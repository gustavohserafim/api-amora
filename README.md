# API de Imóveis e Negociações

Esta API permite a criação e consulta de imóveis e negociações associadas, incluindo a avaliação de risco de cada negociação com base em critérios predefinidos.

https://docs.google.com/document/d/1RaPrdKd8-c7JJQYuIpNMuWfTiL1Qv7-3Qqiy6ixDfX0/edit?tab=t.0

---

## Pré-requisitos
- Docker  27.3

- Docker Compose 2.30
- Python 3.12

## Como rodar
Com o docker e docker-compose instalados, execute na raiz do projeto :
- `docker-compose build`
- `docker-compose up -d`

Serão gerado dois containers, um com o banco de dados postgres e outro com a api.
## Testes
Arquivo contendo os testes:

`tests/test_main.py`

Com o python devidamente instalado na raiz do projeto execute:

- `python -m venv venv`
- `pip install -r requirement.txt`
- `pytest tests/test_main.py`



## **Endpoints**

### **1. Criar Imóvel e Negociação**

**POST** `/imoveis`

Cria um imóvel e a negociação associada, avaliando o risco da negociação.

#### **Requisição**
```json
{
  "realty": {
    "address": "Rua Exemplo, 123",
    "description": "Casa com 3 quartos e piscina.",
    "price": 1000000
  },
  "negotiation": {
    "score": 750,
    "income": 15000
  }
}
```
#### **Resposta**
````json
{
  "id": 1,
  "address": "Rua Exemplo, 123",
  "description": "Casa com 3 quartos e piscina.",
  "price": 1000000,
  "risk_evaluation": true
}
````

Regras de Avaliação de Risco
A negociação será reprovada se:

O valor do imóvel for maior que 10 milhões ou menor que 100 mil reais.
A pontuação de crédito do comprador for inferior a 500.
O valor do imóvel dividido em 360 (parcelas) for maior que 30% da renda mensal do comprador.

### **2. Consultar Negociação por ID**
**GET** `/imoveis/{id}`

Retorna os detalhes do imóvel e da negociação, incluindo o resultado da avaliação de risco.

**Parâmetros**
id (int): ID da negociação.

#### **Resposta**
```json
{
  "id": 1,
  "address": "Rua Exemplo, 123",
  "description": "Casa com 3 quartos e piscina.",
  "price": 1000000,
  "risk_evaluation": true
}
```
**Erros**

404 Not Found:
```json
{
  "detail": "Negotiation not found"
}
```
### **3. Listar Todos os Imóveis** ###
**GET** `/imoveis`

Retorna a lista de todos os imóveis cadastrados.
```json
[
  {
    "id": 1,
    "address": "Rua Exemplo, 123",
    "description": "Casa com 3 quartos e piscina.",
    "price": 1000000,
    "risk_evaluation": true
  },
  {
    "id": 2,
    "address": "Avenida Central, 456",
    "description": "Apartamento com 2 quartos.",
    "price": 800000,
    "risk_evaluation": false
  }
]
```