from src.functions import json_category_product_print
from src.product import Product
from src.category import Category


def main():
    # json_category_product_print()

    product1 = Product("Манго", "Египетское", 300, 20)
    product2 = Product("Мандарины", "Марроко", 150, 30)
    product3 = Product("Бананы", "Эквадор", 159, 35)
    category1 = Category("Фрукты", "Фрукты импортные", [product1, product2])
    # category1.product.append(product3)
    category1.product = product3
    print(category1.product)



if __name__ == "__main__":
    main()
