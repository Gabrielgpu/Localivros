import json
import requests

def create_product(model, access_token):
    url = "https://bling.com.br/Api/v3/produtos"

    payload = json.dumps({
    "nome": f"{model.description}",
    "tipo": "P",
    "situacao": "A",
    "formato": "S",
    "id": "",
    "codigo": f"{model.code}",
    "preco": f"{model.price}",
    "descricaoCurta": f"{model.short_description}",
    "dataValidade": "",
    "unidade": "UN",
    "pesoLiquido": "300",
    "pesoBruto": "300",
    "volumes": "",
    "itensPorCaixa": "",
    "gtin": f"{model.gtin_ean}",
    "gtinEmbalagem": f"{model.gtin_ean}",
    "tipoProducao": "T",
    "condicao": "2",
    "freteGratis": "",
    "marca": f"{model.mark}",
    "descricaoComplementar": "",
    "linkExterno": "",
    "observacoes": "",
    "descricaoEmbalagemDiscreta": "",
    "categoria": {
        "id": f"{model.product_category}"
    },
    "estoque": {
        "minimo": 0.0,
        "maximo": 0.0,
        "crossdocking": 0,
        "localizacao": f"{model.code}"
    },
    "actionEstoque": "Z",
    "dimensoes": {
        "largura": f"{model.width}",
        "altura": f"{model.height}",
        "profundidade": f"{model.depth}",
        "unidadeMedida": 1
    },
    "tributacao": {
        "origem": "",
        "nFCI": "",
        "ncm": "4901.99.00",
        "cest": "",
        "codigoListaServicos": "",
        "spedTipoItem": "",
        "codigoItem": "",
        "percentualTributos": "",
        "valorBaseStRetencao": "",
        "valorStRetencao": "",
        "valorICMSSubstituto": "",
        "codigoExcecaoTipi": "",
        "classeEnquadramentoIpi": "",
        "valorIpiFixo": "",
        "codigoSeloIpi": "",
        "valorPisFixo": "",
        "valorCofinsFixo": "",
        "codigoANP": "",
        "descricaoANP": "",
        "percentualGLP": "",
        "percentualGasNacional": "",
        "percentualGasImportado": "",
        "valorPartida": "",
        "tipoArmamento": 0,
        "descricaoCompletaArmamento": "",
        "dadosAdicionais": "",
        "grupoProduto": {
        "id": ""
        }
    },
    "midia": {
        "video": {
        "url": ""
        },
        "imagens": {
        "imagensURL": [
            {
            "link": f"{model.url_external_images}"
            },
            {
            "link": ""
            }
        ],
        "internas": [
            {
            "linkMiniatura": "",
            "validade": "",
            "ordem": "",
            "anexo": {
                "id": ""
            },
            "anexoVinculo": {
                "id": ""
            }
            },
            {
            "linkMiniatura": "",
            "validade": "",
            "ordem": "",
            "anexo": {
                "id": ""
            },
            "anexoVinculo": {
                "id": ""
            }
            }
        ]
        }
    },
    "linhaProduto": {
        "id": ""
    },
    "estrutura": {
        "tipoEstoque": "F",
        "lancamentoEstoque": "M",
        "componentes": [
        {
            "produto": {
            "id": ""
            },
            "quantidade": ""
        },
        {
            "produto": {
            "id": ""
            },
            "quantidade": ""
        }
        ]
    },
    "camposCustomizados": [
        {
        "idCampoCustomizado": "2044263",
        "idVinculo": "",
        "valor": f"{model.year_published}",
        "item": "Ano de publicação"
        },
        {
        "idCampoCustomizado": "2044265",
        "idVinculo": "",
        "valor": f"{model.page_of_number}",
        "item": "Número de páginas"
        },
        {
        "idCampoCustomizado": "2044269",
        "idVinculo": "",
        "valor": f"{model.additional_information}",
        "item": "Edição"
        },
        {
        "idCampoCustomizado": "2044270",
        "idVinculo": "",
        "valor": f"{model.author}",
        "item": "Autor"
        },
        {
        "idCampoCustomizado": "2094123",
        "idVinculo": "",
        "valor": "173072312",
        "item": "Loja"
        },
        {
        "idCampoCustomizado": "2638758",
        "idVinculo": "",
        "valor": f"{model.year_published}",
        "item": "Data de publicação"
        },
    ],
    "variacoes": [
        {
        "formato": "S",
        "nome": "",
        "situacao": "A",
        "tipo": "P",
        "variacao": {
            "nome": "",
            "ordem": "",
            "produtoPai": {
            "cloneInfo": "",
            "id": ""
            },
            "atributos": "consectetur"
        },
        "id": "",
        "codigo": "",
        "preco": "",
        "descricaoCurta": "",
        "imagemURL": "",
        "dataValidade": "",
        "unidade": "",
        "pesoLiquido": "",
        "pesoBruto": "",
        "volumes": "",
        "itensPorCaixa": "",
        "gtin": "",
        "gtinEmbalagem": "",
        "tipoProducao": "",
        "condicao": "",
        "freteGratis": "",
        "marca": "",
        "descricaoComplementar": "",
        "linkExterno": "",
        "observacoes": "",
        "descricaoEmbalagemDiscreta": "",
        "categoria": {
            "id": ""
        },
        "estoque": {
            "minimo": "",
            "maximo": "",
            "crossdocking": "",
            "localizacao": ""
        },
        "actionEstoque": "T",
        "dimensoes": {
            "largura": "",
            "altura": "",
            "profundidade": "",
            "unidadeMedida": 0
        },
        "tributacao": {
            "origem": "",
            "nFCI": "",
            "ncm": "",
            "cest": "",
            "codigoListaServicos": "",
            "spedTipoItem": "",
            "codigoItem": "",
            "percentualTributos": "",
            "valorBaseStRetencao": "",
            "valorStRetencao": "",
            "valorICMSSubstituto": "",
            "codigoExcecaoTipi": "",
            "classeEnquadramentoIpi": "",
            "valorIpiFixo": "",
            "codigoSeloIpi": "",
            "valorPisFixo": "",
            "valorCofinsFixo": "",
            "codigoANP": "",
            "descricaoANP": "",
            "percentualGLP": "",
            "percentualGasNacional": "",
            "percentualGasImportado": "",
            "valorPartida": "",
            "tipoArmamento": 0,
            "descricaoCompletaArmamento": "",
            "dadosAdicionais": "",
            "grupoProduto": {
            "id": ""
            }
        },
        "midia": {
            "video": {
            "url": ""
            },
            "imagens": {
            "imagensURL": [
                {
                "link": ""
                },
                {
                "link": ""
                }
            ],
            "internas": [
                {
                "linkMiniatura": "",
                "validade": "",
                "ordem": "",
                "anexo": {
                    "id": ""
                },
                "anexoVinculo": {
                    "id": ""
                }
                },
                {
                "linkMiniatura": "",
                "validade": "",
                "ordem": "",
                "anexo": {
                    "id": ""
                },
                "anexoVinculo": {
                    "id": ""
                }
                }
            ]
            }
        },
        "linhaProduto": {
            "id": ""
        },
        "estrutura": {
            "tipoEstoque": "F",
            "lancamentoEstoque": "P",
            "componentes": [
            {
                "produto": {
                "id": ""
                },
                "quantidade": ""
            },
            {
                "produto": {
                "id": ""
                },
                "quantidade": ""
            }
            ]
        },
        "camposCustomizados": [
            {
            "idCampoCustomizado": "",
            "idVinculo": "",
            "valor": "",
            "item": ""
            },
            {
            "idCampoCustomizado": "",
            "idVinculo": "",
            "valor": "",
            "item": ""
            }
        ]
        },
        {
        "formato": "E",
        "nome": "",
        "situacao": "A",
        "tipo": "N",
        "variacao": {
            "nome": "",
            "ordem": "",
            "produtoPai": {
            "cloneInfo": "",
            "id": ""
            },
            "atributos": ""
        },
        "id": "",
        "codigo": "",
        "preco": "",
        "descricaoCurta": "",
        "imagemURL": "",
        "dataValidade": "",
        "unidade": "",
        "pesoLiquido": "",
        "pesoBruto": "",
        "volumes": "",
        "itensPorCaixa": "",
        "gtin": "",
        "gtinEmbalagem": "",
        "tipoProducao": "P",
        "condicao": "",
        "freteGratis": "",
        "marca": "",
        "descricaoComplementar": "",
        "linkExterno": "",
        "observacoes": "",
        "descricaoEmbalagemDiscreta": "",
        "categoria": {
            "id": ""
        },
        "estoque": {
            "minimo": "",
            "maximo": "",
            "crossdocking": "",
            "localizacao": ""
        },
        "actionEstoque": "T",
        "dimensoes": {
            "largura": "",
            "altura": "",
            "profundidade": "",
            "unidadeMedida": ""
        },
        "tributacao": {
            "origem": "",
            "nFCI": "",
            "ncm": "",
            "cest": "",
            "codigoListaServicos": "",
            "spedTipoItem": "",
            "codigoItem": "",
            "percentualTributos": "",
            "valorBaseStRetencao": "",
            "valorStRetencao": "",
            "valorICMSSubstituto": "",
            "codigoExcecaoTipi": "",
            "classeEnquadramentoIpi": "",
            "valorIpiFixo": "",
            "codigoSeloIpi": "",
            "valorPisFixo": "",
            "valorCofinsFixo": "",
            "codigoANP": "",
            "descricaoANP": "",
            "percentualGLP": "",
            "percentualGasNacional": "",
            "percentualGasImportado": "",
            "valorPartida": "",
            "tipoArmamento": "",
            "descricaoCompletaArmamento": "",
            "dadosAdicionais": "",
            "grupoProduto": {
            "id": ""
            }
        },
        "midia": {
            "video": {
            "url": ""
            },
            "imagens": {
            "imagensURL": [
                {
                "link": ""
                },
                {
                "link": ""
                }
            ],
            "internas": [
                {
                "linkMiniatura": "",
                "validade": "",
                "ordem": "",
                "anexo": {
                    "id": ""
                },
                "anexoVinculo": {
                    "id": ""
                }
                },
                {
                "linkMiniatura": "",
                "validade": "",
                "ordem": "",
                "anexo": {
                    "id": ""
                },
                "anexoVinculo": {
                    "id": ""
                }
                }
            ]
            }
        },
        "linhaProduto": {
            "id": ""
        },
        "estrutura": {
            "tipoEstoque": "F",
            "lancamentoEstoque": "P",
            "componentes": [
            {
                "produto": {
                "id": ""
                },
                "quantidade": ""
            },
            {
                "produto": {
                "id": ""
                },
                "quantidade": ""
            }
            ]
        },
        "camposCustomizados": [
            {
            "idCampoCustomizado": "",
            "idVinculo": "",
            "valor": "",
            "item": ""
            },
            {
            "idCampoCustomizado": "",
            "idVinculo": "",
            "valor": "",
            "item": ""
            }
        ]
        }
    ]
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.post(url, headers=headers, data=payload)

    return response





def increment_stock(model, access_token):
    url = "https://bling.com.br/Api/v3/estoques"

    payload = json.dumps({
        "deposito": {
        "id": "14888291425"
        },
        "operacao": "B",
        "produto": {
        "id": f"{model.id_bling}"
        },
        "quantidade": f"{model.stock}",
        "preco": f"{model.price}",
        "custo": f"{model.price}",
        "observacoes": ""
    })

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}',
    }

    response = requests.post(url, headers=headers, data=payload)

    return response