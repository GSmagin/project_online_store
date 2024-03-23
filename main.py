from src.functions import json_category_product_print
from src.product import Product
from src.category import Category
from src.categoryiterator import CategoryIterator



def main():
    # json_category_product_print()

    product1 = Product("Манго", "Египетское", 20, 20)
    product2 = Product("Мандарины", "Марроко", 150, 25)
    product3 = Product("Бананы", "Эквадор", 165, 65)
    category1 = Category("Фрукты", "Фрукты импортные", [product1, product2])
    category1.product = product3
    # print(category1.product)
    # print(category1)
    # print(product2 + product3)

    # for product in category1.product:
        # print(product)
    for product in CategoryIterator(category1):
        print(product)



if __name__ == "__main__":
    main()
