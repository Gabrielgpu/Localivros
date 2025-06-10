## 📚 LOCALIVROS

**LOCALIVROS** é uma aplicação web desenvolvida com Django para gerenciamento e integração de dados de livros. O sistema permite cadastrar, visualizar, filtrar e integrar produtos com plataformas externas por meio de APIs REST, mantendo os dados centralizados e atualizados.

---

## Funcionalidades

- Cadastro e listagem de livros
- Busca com código de barras (ISBN)
- Paginação com limite de 10 produtos por páginas
- Integração com plataforma **Bling** via API REST
- Envio manual de dados para marketplace (Bling)
- Rotas protegidas com autenticação (`LoginRequiredMixin`)
- Exibição dos 5 últimos produtos cadastrados na página inicial

---

## Tecnologias utilizadas

- [Python 3.12+](https://www.python.org)
- [Django 5.2+](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- SQLite
- HTML5, CSS3, Django Templates

---

## ⚙️ Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/localivros.git
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Aplique as migrações:**
```bash
python manage.py migrate
```

4. **Inicie o sistema:**
```bash
python manage.py runsever
```

5. **Acesse a rota para criar um usuario:**
http://127.0.0.1:8000/account/register


## Configuração do Bling (API)
**Para que o sistema possa se comunicar com o Bling (ERP), é necessário criar um arquivo .env na raiz do projeto com as credenciais de acesso à API.**

1. **Criação da Conta**<br>
Se você ainda não possui uma conta no Bling, crie uma gratuitamente para obter sua chave da API.

2. **Arquivo .env**<br>
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
```
EXTERNAL_CLIENT_ID="client_id"
EXTERNAL_CLIENT_SECRET="client_secret"
EXTERNAL_API_URI="http://127.0.0.1:8000/api/v1/auth/bling/callback/"
EXTERNAL_API_TOKEN_ENDPOINT="https://api.bling.com.br/Api/v3/oauth/token"
EXTERNAL_API_AUTHORIZATION_END_POINT="https://bling.com.br/Api/v3/oauth/authorize"
