from src.product import Product
from src.category import Category


def main():
    product1 = Product("Product 1", "Описание", 10, 12)
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)


    product2 = Product("Product 2", "Описание", 10, 12)
if __name__ == "__main__":
    main()
