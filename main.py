from src.product import Product
from src.category import Category
from src.filejson import FileJson
from confing import dir_json
from src.functions import products_json_file
from src.category import Category
from src.product import Product
from src.filejson import FileJson



def main():
    for products_json in products_json_file():
        transaction = FileJson(products_json)
        print(transaction.name)

    #




    # product2 = Product("Манго", "Египетское", 300, 20)
    # product3 = Product("Мандарины", "Марроко", 150, 30)

if __name__ == "__main__":
    main()
