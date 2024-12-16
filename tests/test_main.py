import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.parametrize(
    "realty_data, negotiation_data, expected_result",
    [
        # Cenário 1: Aprovado - imóvel acessível, boa pontuação e renda compatível
        ({"address": "Rua A", "description": "Casa grande", "price": 500000},
         {"score": 750, "income": 15000}, True),

        # Cenário 2: Reprovado - financiamento mensal maior que 30% da renda
        ({"address": "Rua B", "description": "Apartamento", "price": 500000},
         {"score": 700, "income": 4000}, False),

        # Cenário 3: Reprovado - pontuação de crédito baixa
        ({"address": "Rua C", "description": "Apartamento", "price": 400000},
         {"score": 400, "income": 20000}, False),

        # Cenário 4: Reprovado - preço fora do intervalo aceitável
        ({"address": "Rua D", "description": "Mansão", "price": 15000000},
         {"score": 800, "income": 50000}, False),

        # Cenário 5: Aprovado - imóvel barato, pontuação e renda compatíveis
        ({"address": "Rua E", "description": "Casa simples", "price": 200000},
         {"score": 650, "income": 8000}, True),
    ]
)
def test_create_realty(realty_data, negotiation_data, expected_result):
    response = client.post("/imoveis", json={"realty": realty_data, "negotiation": negotiation_data})
    assert response.status_code == 200

    # Verificar o resultado da avaliação de risco
    result = response.json()["risk_evaluation"]
    assert result == expected_result
