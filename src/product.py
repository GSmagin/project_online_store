
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
