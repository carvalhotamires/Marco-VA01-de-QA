def calcular_desconto(valor_compra, tipo_cliente):
    desconto = 0

    # Validação do desconto base (correção: >= 100 em vez de > 100)
    if 100 <= valor_compra < 500:
        desconto = 0.10
    elif valor_compra >= 500:
        desconto = 0.20

    # Validação do cliente VIP (correção: case-insensitive e remoção de espaços)
    if isinstance(tipo_cliente, str) and tipo_cliente.strip().upper() == "VIP":
        desconto += 0.05

    valor_desconto = valor_compra * desconto

    # Regra do Teto de R$ 200,00
    if valor_desconto > 200:
        valor_desconto = 200

    return round(valor_desconto, 2)