import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Манго", "Египетское", 300, 20)


def test_init(sample_product):
    product = sample_product
    assert product.name == "Манго"
    assert product.description == "Египетское"
    assert product.price == 300
    assert product.quantity == 20





