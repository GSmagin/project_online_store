from src.functions import json_category_product_print
from src.product import Product, Smartphone, LawnGrass
from src.category import Category
from src.categoryiterator import CategoryIterator



def main():
    # json_category_product_print()

    product1 = Product("Манго", "Египетское", 20.56, 20)
    product2 = Product("Мандарины", "Марроко", 150, 25)
    product3 = Product("Бананы", "Эквадор", 165, 25)
    category1 = Category("Фрукты", "Фрукты импортные", [product1, product2,  product3])


    smartphone1 = Smartphone("iPhone 13", "Смартфон от Apple", 999.18,
                             20, "Высокая", "13", 128, "черный")
    smartphone2 = Smartphone("Samsung Galaxy S21", "Смартфон от Samsung",
                             899.0, 15, "Средняя", "S21", 256, "синий")

    lawn_grass1 = LawnGrass("Bluegrass", "Высококачественная трава для газонов", 10.0, 100, "США", 14, "зеленый")

    category2 = Category("Смартфоны", "Мобильные телефоны", [smartphone1, smartphone2])

    print(category1.average_price())
    category = Category("", "", "")
    print(category.average_price())




if __name__ == "__main__":
    main()
