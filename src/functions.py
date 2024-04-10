import json
from confing import dir_json
from src.product import Product
from src.category import Category


def load_json(file_path=dir_json):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def json_category_product(data=load_json()):
    categories = []
    for category_data in data:
        category_name = category_data["name"]
        category_description = category_data["description"]
        category_products = []

        for product_data in category_data["products"]:
            product_name = product_data["name"]
            product_description = product_data["description"]
            product_price = product_data["price"]
            product_quantity = product_data["quantity"]

            product = Product(product_name, product_description, product_price, product_quantity)
            category_products.append(product)

        category = Category(category_name, category_description, category_products)
        categories.append(category)

    return categories


def json_category_product_print():
    """Выводит информацию о категориях и их продуктах"""

    for category in json_category_product():
        print("Категория:", category.name)
        print("Описание:", category.description)
        print("Продукты в категории:")
        for product in category.products:
            print("- Название:", product.name)
            print("  Описание:", product.description)
            print("  Цена:", product.price)
            print("  Количество:", product.quantity)
        print()
