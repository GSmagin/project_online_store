import pytest
from src.classifiers import *


@pytest.fixture
def sample_product():
    return Product("Книга", "Художественная литература", 15.99, 100)


@pytest.fixture
def sample_category():
    return Category("Книги", "Книги всех жанров")


def test_product_initialization(sample_product):
    assert sample_product.name == "Книга"
    assert sample_product.description == "Художественная литература"
    assert sample_product.price == 15.99
    assert sample_product.quantity == 100


def test_category_initialization(sample_category):
    assert sample_category.name == "Книги"
    assert sample_category.description == "Книги всех жанров"


def test_add_product(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert sample_product in sample_category.products


def test_remove_product(sample_category, sample_product):
    sample_category.add_product(sample_product)
    sample_category.remove_product(sample_product)
    assert sample_product not in sample_category.products
