import pytest
from tech.tamires.ecommerce.operacoes.calcular_desconto import calcular_desconto


# ====================================================================
# Testes com parametrização (@pytest.mark.parametrize)
# Cobrindo todos os cenários dos Critérios de Aceite
# ====================================================================

@pytest.mark.parametrize(
    "valor_compra, tipo_cliente, resultado_esperado",
    [
        # Faixa 1: Compras < 100 (0% base)
        (50.00, "COMUM", 0.00),         # Cliente comum sem desconto
        (99.99, "COMUM", 0.00),         # Limite superior da faixa de 0%
        (80.00, "VIP", 4.00),           # VIP recebe 5% extra mesmo abaixo de 100 (5% de 80 = 4.00)

        # Faixa 2: Compras >= 100 e < 500 (10% base)
        (100.00, "COMUM", 10.00),       # Limite exato de 100: deve receber 10% (R$ 10,00)
        (100.00, "VIP", 15.00),         # Limite exato de 100 com VIP: 15% (R$ 15,00)
        (300.00, "COMUM", 30.00),       # Cenário testado "de cabeça" pelo Dev Jr.
        (300.00, "VIP", 45.00),         # 300 com VIP: 15% (R$ 45,00)
        (499.99, "COMUM", 50.00),       # Limite superior da faixa de 10% (round(49.999, 2) = 50.00)

        # Faixa 3: Compras >= 500 (20% base)
        (500.00, "COMUM", 100.00),      # Limite exato de 500: recebe 20% (R$ 100,00)
        (500.00, "VIP", 125.00),        # Limite exato de 500 com VIP: 25% (R$ 125,00)
        (800.00, "COMUM", 160.00),      # Compra alta comum: 20% de 800 (R$ 160,00)

        # Faixa 4: Regra de Teto (máximo R$ 200,00)
        (800.00, "VIP", 200.00),        # 25% de 800 = 200 (atinge o teto exato)
        (1000.00, "VIP", 200.00),       # 25% de 1000 = 250 -> limitado a 200
        (1500.00, "COMUM", 200.00),     # 20% de 1500 = 300 -> limitado a 200
        (2000.00, "VIP", 200.00),       # 25% de 2000 = 500 -> limitado a 200
    ],
)
def test_calcular_desconto_faixas_e_teto(valor_compra, tipo_cliente, resultado_esperado):
    """Testa os valores esperados para diferentes faixas de compra, tipos de cliente e teto."""
    resultado = calcular_desconto(valor_compra, tipo_cliente)
    assert resultado == resultado_esperado


@pytest.mark.parametrize(
    "tipo_vip, valor_compra, resultado_esperado",
    [
        ("VIP", 200.00, 30.00),         # Todo em maiúsculas
        ("vip", 200.00, 30.00),         # Todo em minúsculas
        ("Vip", 200.00, 30.00),         # Primeira maiúscula
        ("vIp", 200.00, 30.00),         # Alternado
        (" VIP ", 200.00, 30.00),       # Com espaços nas pontas
    ],
)
def test_calcular_desconto_cliente_vip_case_insensitive(tipo_vip, valor_compra, resultado_esperado):
    """Testa a regra de que VIP deve funcionar independente de maiúsculas ou minúsculas."""
    resultado = calcular_desconto(valor_compra, tipo_vip)
    assert resultado == resultado_esperado
