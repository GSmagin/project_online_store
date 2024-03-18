from src.functions import json_category_product_print
from src.product import Product
from src.category import Category


def main():
    json_category_product_print()

    product1 = Product("Манго", "Египетское", 300, 20)
    product2 = Product("Мандарины", "Марроко", 150, 30)

    category1 = Category("Фрукты", "Фрукты импортные", [product1, product2])
    print(category1.total_categories)
    print(category1.total_unique_products)
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)


if __name__ == "__main__":
    main()
