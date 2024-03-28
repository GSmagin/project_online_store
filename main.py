from src.functions import json_category_product_print
from src.product import Product, Smartphone, LawnGrass
from src.category import Category
from src.categoryiterator import CategoryIterator



def main():
    # json_category_product_print()

    product1 = Product("Манго", "Египетское", 20, 20)
    product2 = Product("Мандарины", "Марроко", 150, 25)
    product3 = Product("Бананы", "Эквадор", 165, 65)
    category1 = Category("Фрукты", "Фрукты импортные", [product1, product2,  product3])
    # category1.product = product3
    # print(category1.product)
    # print(category1)
    # print(product2 + product3)

    # for product in category1.product:
        # print(product)
    # for product in CategoryIterator(category1):
    #     print(product)

    smartphone1 = Smartphone("iPhone 13", "Смартфон от Apple", 999.0,
                             20, "Высокая", "13", 128, "черный")
    smartphone2 = Smartphone("Samsung Galaxy S21", "Смартфон от Samsung",
                             899.0, 15, "Средняя", "S21", 256, "синий")

    lawn_grass1 = LawnGrass("Bluegrass", "Высококачественная трава для газонов", 10.0, 100, "США", 14, "зеленый")

    category2 = Category("Смартфоны", "Мобильные телефоны", [smartphone1, smartphone2])
    result_category = category2 + smartphone1
    print(result_category.products_format)


    result_smartphone = smartphone1 + smartphone2
    print("Сумма товаров:", result_smartphone)

    print(isinstance(product3, Product))


    # iterator1 = CategoryIterator(category1)
    #
    # for product in iterator1:
    #     # print(product)
    #     print(f"Name: {product.get("name")},"
    #           f" Description: {product.get("description")},"
    #           f" Category: {product.get("category")},"
    #           f" Price: {product.get("price")}")
    # print(category1)


if __name__ == "__main__":
    main()
