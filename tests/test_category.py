import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Манго", "Египетское", 300, 20)


def test_init(sample_product):
    category = Category("Фрукты", "Категория для фруктов", [sample_product])
    assert category.name == "Фрукты"
    assert category.description == "Категория для фруктов"



