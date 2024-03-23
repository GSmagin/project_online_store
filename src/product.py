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
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Результат сложения двух продуктов, умноженных на количество на складе"""
        return (self.__price * self.quantity) + (other.price * other.quantity)



    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не может быть меньше или равно 0")
            raise ValueError("Цена не может быть меньше или равно 0")
        else:
            self.__price = new_price


