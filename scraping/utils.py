
from playwright.async_api import async_playwright
from selectolax.parser import HTMLParser
from amazoncaptcha import AmazonCaptcha
from rich import print
import datetime
import re
import asyncio


class WebScraping:
    def __init__(self):
        self.url = None
        self.playwright = None
        self.asin = None
        self.page = None
        self.html = None
        self.index = 0
        self.browser = None
        self.book_inf = None

    def get_index(self):
        return self.index

    def set_asin(self, asin):
        self.asin = asin

    async def start_browser(self):
        try:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=True)
            self.page = await self.browser.new_page()
        except Exception as e:
            print(f"Erro ao iniciar o navegador: {e}")
            await self.close_browser()

    async def get_html(self):
        print("Chegou dentro do método get_html")
        try:
            print("Tentando acessar a URL")
            await asyncio.wait_for(self.page.goto(self.url + self.asin), timeout=60)
            print("Acesso à URL concluído")
            
            captcha_element = await self.page.query_selector('//*[@id="captchacharacters"]')
            if captcha_element:
                print("Captcha encontrado")
                await self.pass_captcha(captcha_element)
                await asyncio.sleep(3)

            content = await self.page.content()
            self.html = HTMLParser(content)
            
        except asyncio.TimeoutError:
            print("Timeout ao tentar obter o HTML da página.")
        except Exception as e:
            print(f"Erro ao obter HTML: {e}")

    def create(self):
        book_data = BookData()
        self.book_inf = book_data.to_dict()

    async def close_browser(self):
        try:
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
        except Exception as e:
            print(f"Erro ao fechar o navegador: {e}")

    async def pass_captcha(self, captcha_element):
        while captcha_element is not None:
            image_element = await self.page.query_selector("//div[@class='a-row a-spacing-large']//img")
            if image_element:
                image = await image_element.get_attribute('src')
                captcha = AmazonCaptcha.fromlink(image)
                captcha_value = AmazonCaptcha.solve(captcha)
                print(captcha_value)
                input_element = await self.page.query_selector("//div[@class='a-row a-spacing-base']//input")
                if input_element:
                    await input_element.fill(captcha_value)
                    await self.page.click("//div[@class='a-section a-spacing-extra-large']//button")
                    print("Tentando passar por um bloqueio da Amazon...")
            captcha_element = await self.page.query_selector('//*[@id="captchacharacters"]')

    def get_text(self, selector):
        element = self.html.css_first(selector)
        return element.text(strip=True) if element else ''

    async def parse_html(self):
        try:

            print(f"Length do ASIN: {len(self.asin)}")
            print(type(self.asin))
            asin = self.asin
            if len(asin) > 10:
                print(f"Modo teste: {asin}")
                dados = await self.page.query_selector('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[1]/span/a')
                dados = await dados.get_attribute("href")
                print(f"ASIN: {dados.split("/")[3]}")

                asin = dados.split("/")[3]
                # time.sleep(5)
                self.url = "https://www.amazon.com.br/dp/"
                await asyncio.wait_for(self.page.goto(self.url + asin), timeout=60)
                content = await self.page.content()
                self.html = HTMLParser(content)


            self.book_inf["Descrição"].append(self.get_text('#productTitle'))
            self.book_inf["Descrição_Curta"].append(self.get_text('#bookDescription_feature_div .a-expander-partial-collapse-content'))
            self.book_inf["numeroDePaginas"].append(self.get_text('#rpi-attribute-book_details-fiona_pages .rpi-attribute-value span').split(" ")[0])
            self.book_inf["idioma"].append(self.get_text('#rpi-attribute-language .rpi-attribute-value span'))
            self.book_inf["Marca"].append(self.get_text('#rpi-attribute-book_details-publisher .rpi-attribute-value span'))
            self.book_inf["anoDePublicacao"].append(self.mes_por_extenso_para_numero(self.get_text('#rpi-attribute-book_details-publication_date .rpi-attribute-value span')))
            self.book_inf["isbn10"].append(self.get_text('#rpi-attribute-book_details-isbn10 .rpi-attribute-value span'))
            self.book_inf["GTIN_EAN"].append(self.get_text('#rpi-attribute-book_details-isbn13 .rpi-attribute-value span').replace("-", ""))
            self.book_inf["GTIN_EAN_embalagem"].append(self.get_text('#rpi-attribute-book_details-isbn13 .rpi-attribute-value span').replace("-", ""))
            self.book_inf["autor"].append(self.get_text('#bylineInfo .a-link-normal'))
            self.book_inf["Categoria_produto"].append(self.get_text('li:nth-child(5) .a-color-tertiary'))
            preco_incompleto = self.get_text('.aod-popover-caret-link').split(" ")[-1]
            preco_completo = [number for number in preco_incompleto if number.isnumeric() or number == ","]
            self.book_inf["Preço"].append("".join(preco_completo).replace(',', '.'))
            self.book_inf["Preço_novo"].append(self.get_text('.aok-offscreen').split(" ")[0][-5:])
            dimension = self.get_text('#rpi-attribute-book_details-dimensions .rpi-attribute-value span')
            height, width, depth = self.unpack_dimension(dimension)
            await self.search_edition()
            self.book_inf["Largura"].append(width)
            self.book_inf["Altura"].append(height)
            self.book_inf["Profundidade"].append(depth)
        except Exception as e:
            print(f"Erro ao analisar o HTML: {e}")
    
    def mes_por_extenso_para_numero(self, mes):
        meses_por_extenso = {
            'janeiro': '01',
            'fevereiro': '02',
            'março': '03',
            'abril': '04',
            'maio': '05',
            'junho': '06',
            'julho': '07',
            'agosto': '08',
            'setembro': '09',
            'outubro': '10',
            'novembro': '11',
            'dezembro': '12',
        }


        list_mes = mes.split(" ")
        
        if len(list_mes) == 3:
            list_mes[1] = meses_por_extenso[list_mes[1]]
            return datetime.date(int(list_mes[2]), int(list_mes[1]), int(list_mes[0])).strftime("%Y-%m-%d")

        return ""

    def unpack_dimension(self, dimension):
        try:
            width, height, depth = dimension.split("x")
            depth = depth.replace("cm", "")
        except ValueError:
            width, height, depth = "", "", ""
        return width, height, depth

    async def search_image(self):
        try:
            img_element = await self.page.query_selector("#imgTagWrapperId img")
            image = await img_element.get_attribute('src') if img_element else ''
            self.book_inf["URL_Imagens_Externas"].append(image)
        except Exception as e:
            print(f"Erro ao buscar imagem: {e}")

    async def search_edition(self):
        try:
            print('Acessando as informações adicionais...')
            text = await self.page.query_selector('//span[@class="a-list-item"]/span[2]')
            edition = await text.inner_text() if text else ""
            print("Texto do edição:", edition)
            edition = re.search(r'(\d+)(?:ª|ª\s)edição', edition)
            if edition:
                edition = edition.group(1) + 'ª' + " Edição"
            else:
                edition = ''
            self.book_inf["Informações_adicionais"].append(edition)
        except Exception as e:
            print(f"Erro ao buscar edição: {e}")

    async def display(self):
        print({
            "Titulo": self.book_inf["Descrição"],
            "Descrição": self.book_inf["Descrição_Curta"],
            "Autor": self.book_inf["autor"],
            "Imagem": self.book_inf["URL_Imagens_Externas"],
            "Paginas": self.book_inf["numeroDePaginas"],
            "Idioma": self.book_inf["idioma"],
            "Editora": self.book_inf["Marca"],
            "Data de Publicação": self.book_inf["anoDePublicacao"],
            "ISBN10": self.book_inf["isbn10"],
            "ISBN13": self.book_inf["GTIN_EAN"],
            "Altura": self.book_inf["Altura"],
            "Largura": self.book_inf["Largura"],
            "Profundidade": self.book_inf["Profundidade"],
            "Edição": self.book_inf['Informações_adicionais'],
            "Preço": self.book_inf['Preço'],
            "Preço Novo": self.book_inf['Preço_novo'],
            "Categoria": self.book_inf["Categoria_produto"]
        })
    
    async def result(self):
        return {
            "gtin_ean": self.book_inf["GTIN_EAN"][0], 
            "title": self.book_inf["Descrição"][0], 
            "author": self.book_inf["autor"][0], 
            "short_description": self.book_inf["Descrição_Curta"][0], 
            "url_external_images": self.book_inf["URL_Imagens_Externas"][0], 
            "price": self.book_inf["Preço"][0], 
            "sku": "", 
            "page_of_number": self.book_inf["numeroDePaginas"][0], 
            "editora": self.book_inf["Marca"][0], 
            "year_published": self.book_inf["anoDePublicacao"][0], 
            "height": self.book_inf["Altura"][0], 
            "width": self.book_inf["Largura"][0], 
            "depth": self.book_inf["Profundidade"][0], 
            "mark": self.book_inf['Informações_adicionais'][0],
           "Preço Novo": self.book_inf['Preço_novo'][0],
            "product_category": self.book_inf["Categoria_produto"][0]
        }

class ScraperManager:
  def __init__(self):
    self.scraping = None

  async def start_first_part(self):
    try:
      self.scraping = await start_scraping(parte=1)
    except Exception as e:
      print(f"Erro ao iniciar a primeira parte: {e}")

  async def start_second_part(self, isbn_13):
    try:
      isbn_converter = IsbnConverter(isbn_13)
      isbn_10 = isbn_converter.isbn13_to_isbn10()

      if self.scraping is None:
          raise RuntimeError("O navegador não foi inicializado. Execute a primeira parte primeiro.")
      book = await start_scraping(isbn=isbn_10, parte=2, scrap=self.scraping)
      return book
    except Exception as e:
      print(f"Erro ao iniciar a segunda parte: {e}")

  async def close(self):
    if self.scraping is not None:
      try:
        await self.scraping.close_browser()
        self.scraping = None
      except Exception as e:
        print(f"Erro ao fechar o navegador: {e}")


async def start_scraping(isbn=None, parte=1, scrap=None):
    try:
        if parte == 1:
            scraping = WebScraping()
            scraping.url = 'https://www.amazon.com.br/dp/'
            
            await scraping.start_browser()
            return scraping
        else:
            if scrap is None:
                raise ValueError("O objeto de scraping não pode ser None para a parte 2.")
            
            if len(isbn) > 10:
                scrap.url = "https://www.amazon.com.br/"
                isbn = "s?k=" + isbn + "&__mk_pt_BR=ÅMÅŽÕÑ&ref=nb_sb_noss"
            else:
                scrap.url = 'https://www.amazon.com.br/dp/'

            scrap.create()
            scrap.set_asin(isbn)
            
            await scrap.get_html()
            await scrap.parse_html()
            await scrap.search_image()
            
            await scrap.display()
            result = await scrap.result()
            
            return result
    except Exception as e:
        print(f"Erro no processo de scraping: {e}")
        return ""








class IsbnConverter():

  def __init__(self, isbn_13):
    self.isbn_13 = isbn_13

  
  def isbn13_to_isbn10(self):
    self.isbn_13 = str(self.isbn_13)
    if len(self.isbn_13) != 13 or self.isbn_13[:3] != '978':
      print(f"Erro isbn: {self.isbn_13}")
      return self.isbn_13
    
    isbn_10 = self.isbn_13[3:12]
    sum = 0

    for i in range(9):
      sum += int(isbn_10[i]) * (10 - i)
    check_digit = 11 - (sum % 11)
    if check_digit == 10:
      check_digit = 'X'
    elif check_digit == 11:
      check_digit = '0'
    isbn_10 += str(check_digit)
    print(isbn_10)
    return isbn_10




class BookData:
  def __init__(self):
    self.ID = ''
    self.Código = ''
    self.Descrição = []
    self.Unidade = 'UN'
    self.NCM = '4901.99.00'
    self.Origem = ''
    self.Preço_novo = []
    self.Preço = []
    self.Valor_IPI_fixo = ''
    self.Observações = ''
    self.Situação = ''
    self.Estoque = ''
    self.Preço_de_custo = ''
    self.Cód_no_fornecedor = ''
    self.Fornecedor = ''
    self.Localização = ''
    self.Estoque_maximo = ''
    self.Estoque_minimo = ''
    self.Peso_líquido = ''
    self.Peso_bruto = ''
    self.GTIN_EAN = []
    self.GTIN_EAN_embalagem = []
    self.Largura = []
    self.Altura = []
    self.Profundidade = []
    self.Data_Validade = ''
    self.Descrição_no_fornecedor = ''
    self.Descrição_Complementar = ''
    self.Itens_por_caixa = ''
    self.Produto_Variação = ''
    self.Tipo_Produção = ''
    self.Enquadramento_IPI = ''
    self.Código_serviços = ''
    self.Tipo_item = ''
    self.Grupo_Tags = ''
    self.Tributos = ''
    self.Código_Pai = ''
    self.Código_Integração = ''
    self.Grupo_produtos = ''
    self.Marca = []
    self.CEST = ''
    self.Volumes = ''
    self.Descrição_Curta = []
    self.Cross_Docking = ''
    self.URL_Imagens_Externas = []
    self.Link_Externo = ''
    self.Meses_Garantia_Fornecedor = ''
    self.Clonar_dados_pai = ''
    self.Condição_produto = ''
    self.Frete_Grátis = ''
    self.Número_FCI = ''
    self.Video = ''
    self.Departamento = ''
    self.Unidade_medida = ''
    self.Preço_compra = ''
    self.Valor_base_ICMS_ST = ''
    self.Valor_ICMS_ST = ''
    self.Valor_ICMS_substituto = ''
    self.Categoria_produto = []
    self.Informações_adicionais = []
    self.anoDePublicacao = []
    self.numeroDePaginas = []
    self.autor = []
    self.idioma = []
    self.isbn10 = []

  def to_dict(self):
    return self.__dict__.copy()
