import pytest
from unittest.mock import MagicMock
from pedido.pedido import Item, Pedido, contar_frete_gratis


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

#BUG 3, O desconto esta sendo adicionado no preço final e não subtraida 
def test_exemplo_de_desconto(pedido_grande):
    # 2 X-burgers + 2 refrigerantes + 1 batata frita = 73
    assert pedido_grande.total_com_desconto(percentual=50.0) == 36.5

#BUG 4, O item mais barato está retornando o item mais caro
def test_item_mais_barato(pedido_grande):
    # devia retornar refrigerante mas esta retornado X-burger
    assert pedido_grande.item_mais_barato().nome == "Refrigerante"


# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_frete_gratis(pedidos) -> int
# Escreva os testes ANTES de implementar a função
def test_contar_frete_gratis_lista_vazia():
    assert contar_frete_gratis([]) == 0


def test_contar_frete_gratis_todos(pedido_grande, pedido_com_frete):
    pedidos = [pedido_grande, pedido_com_frete]

    assert contar_frete_gratis(pedidos) == 2


def test_contar_frete_gratis_nenhum(pedido_pequeno):
    outro_pedido_pequeno = Pedido("Carlos", [Item("Suco", 10.0, 2)])
    pedidos = [pedido_pequeno, outro_pedido_pequeno]

    assert contar_frete_gratis(pedidos) == 0


def test_contar_frete_gratis_lista_mista(pedido_grande, pedido_pequeno):
    pedidos = [pedido_grande, pedido_pequeno]

    assert contar_frete_gratis(pedidos) == 1

# Requisito 2 — situacao(unidades_indisponiveis) -> str
# Escreva os testes ANTES de implementar o método

def test_situacao_cancela_pedido_com_mais_de_25_por_cento_indisponivel(pedido_grande):
    assert pedido_grande.situacao(unidades_indisponiveis=2) == "Cancelado por falta de estoque"


def test_situacao_confirma_pedido_com_frete_gratis(pedido_grande):
    assert pedido_grande.situacao(unidades_indisponiveis=0) == "Confirmado com frete grátis"


def test_situacao_confirma_pedido_sem_frete_gratis(pedido_pequeno):
    assert pedido_pequeno.situacao(unidades_indisponiveis=0) == "Confirmado"


def test_situacao_com_25_por_cento_indisponivel_segue_regra_do_frete():
    pedido = Pedido("Carlos", [Item("Lanche", 15.0, 4)])

    assert pedido.situacao(unidades_indisponiveis=1) == "Confirmado com frete grátis"


def test_situacao_cancela_pedido_pouco_acima_de_25_por_cento():
    pedido = Pedido("Marina", [Item("Salgado", 1.0, 100)])

    assert pedido.situacao(unidades_indisponiveis=26) == "Cancelado por falta de estoque"

# Requisito 3 — sugerir_frete_gratis(sms_service) -> None
# Use MagicMock para simular o serviço de SMS
# Escreva os testes ANTES de implementar o método
