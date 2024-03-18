import pytest
from src.functions import *


@pytest.fixture
def test_data():
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                }
            ]
        }
    ]
    return data


def test_json_category_product(test_data):
    print(type(json_category_product(test_data)))
    assert json_category_product(test_data).__class__ == list


def test_json_category_product_print():
    json_category_product_print()

