def evaluate_risk(price, score, income) -> bool:
    if price > 10000000 or price < 100000:
        return False  # Rejeita se o preço for muito alto ou muito baixo

    if score < 500:
        return False  # Rejeita se o histórico de crédito for baixo (pontuação < 500)

    if price / 360 > income * 0.30:
        return False  # Rejeita se o preço do imóvel for mais de 30% da renda mensal

    return True  # Aprova se todas as condições forem atendidas
