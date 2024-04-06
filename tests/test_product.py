import pytest
from src.category import Category
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def sample_product():
    return Product("Манго", "Египетское", 300, 20)


@pytest.fixture
def sample_product2():
    return Product("Мандарины", "Марроко", 150, 25)


@pytest.fixture
def sample_product3():
    return Product("Бананы", "Эквадор", 165, 25)


@pytest.fixture
def sample_product_smartphone():
    smartphone1 = Smartphone("iPhone 13", "Смартфон от Apple", 999.0,
                             20, "Высокая", "13", 128, "черный")
    return smartphone1


@pytest.fixture
def sample_product_smartphone2():
    smartphone2 = Smartphone("Samsung Galaxy S21", "Смартфон от Samsung",
                             899.0, 15, "Средняя", "S21", 256, "синий")
    return smartphone2


@pytest.fixture
def sample_product_lawngrass1():
    lawn_grass1 = LawnGrass("Bluegrass", "Высококачественная трава для газонов",
                            10.0, 100, "США", 14, "зеленый")
    return lawn_grass1


def test_init(sample_product):
    product = sample_product
    assert product.name == "Манго"
    assert product.description == "Египетское"
    assert product.price == 300
    assert product.quantity == 20


def test_add(sample_product_smartphone, sample_product_smartphone2, sample_product_lawngrass1):
    smartphone1 = sample_product_smartphone
    smartphone2 = sample_product_smartphone2
    lawn_grass1 = sample_product_lawngrass1
    result_category = smartphone1 + smartphone2
    assert result_category == 33465.0
    with pytest.raises(TypeError):
        result = smartphone1 + lawn_grass1


def test_product_0():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Product("Манго", "Египетское", 300, 0)


def test_product_price_average(sample_product, sample_product2, sample_product3):
    category = Category("Фрукты", "Фрукты импортные",
                        [sample_product, sample_product2, sample_product3])
    assert category.average_price() == 205.0
