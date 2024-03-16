
class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
         :name название
         :description описание
         :price цена
         :quantity количество в наличии
         """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product: Product):
        self.products.append(product)
        Category.total_unique_products.add(product.name)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
            Category.total_unique_products.remove(product.name)
        else:
            print(f"{product.name} is not in {self.name} category.")













