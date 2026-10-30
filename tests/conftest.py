import pytest
from pedido.pedido import Item, Pedido

@pytest.fixture
def pedido_pequeno():
    return Pedido(
        cliente="Bruno",
        itens=[
            Item("Café", 6.0, 1),
            Item("Pão de queijo", 4.5, 2),
        ],
    )

@pytest.fixture
def pedido_grande():
    return Pedido(
        cliente="Ana",
        itens=[
            Item("X-burguer", 22.0, 2),
            Item("Refrigerante", 7.0, 2),
            Item("Batata frita", 15.0, 1),
        ],
    )

@pytest.fixture
def pedido_com_frete():
    return Pedido(
        cliente = "Victor",
        itens=[
            Item("X-Cupim",50.0,1),
        ], 
    )

