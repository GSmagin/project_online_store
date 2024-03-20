from src.functions import json_category_product_print
from src.product import Product
from src.category import Category


def main():
    # json_category_product_print()

    product1 = Product("Манго", "Египетское", 20, 20)
    product2 = Product("Мандарины", "Марроко", 150, 30)
    product3 = Product("Бананы", "Эквадор", 159, 35)
    category1 = Category("Фрукты", "Фрукты импортные", [product1, product2])
    category1.product = product3
    print(category1.product)
    category1.product = Product.new_product("Бананы1", "Эквадор1", 159, 35)
    print(category1.product)
    print(category1.products_format)
    product1.price = 20
    print(product1.price)


if __name__ == "__main__":
    main()
