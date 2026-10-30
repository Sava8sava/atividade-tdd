import pytest
from unittest.mock import MagicMock
from pedido.pedido import Item, Pedido


# =============================================================
# EXEMPLO — um teste pronto, para você copiar o formato
# =============================================================

def test_exemplo_quantidade_total(pedido_pequeno):
    # 1 café + 2 pães de queijo = 3 unidades
    assert pedido_pequeno.quantidade_total() == 3


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug. Cada teste deve FALHAR
# no código original. Não altere src/pedido/pedido.py ainda.
# =============================================================

#BUG 1, as regra dizem que o frete é valido para valores a partir de 50 reais mas o cliente só ganha quando é maior que 50
def test_frete_apartir_de_50_reais(pedido_com_frete):
    assert pedido_com_frete.tem_frete_gratis() == True

#BUG 2, O subtotal não está multiplicando o preço pela quantidade de cada item
def test_subtotal_considera_quantidade(pedido_grande):
    # (22.0 * 2) + (7.0 * 2) + (15.0 * 1) = 73.0
    assert pedido_grande.subtotal() == 73.0



# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_frete_gratis(pedidos) -> int
# Escreva os testes ANTES de implementar a função



# Requisito 2 — situacao(unidades_indisponiveis) -> str
# Escreva os testes ANTES de implementar o método



# Requisito 3 — sugerir_frete_gratis(sms_service) -> None
# Use MagicMock para simular o serviço de SMS
# Escreva os testes ANTES de implementar o método
