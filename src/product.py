from abc import ABC, abstractmethod


class ReprMixin:
    def __repr__(self):
        attributes = ', '.join([f"{value}" for key, value in self.__dict__.items()])
        return f"{attributes}"


class AbstractProduct(ABC):
    """ Базовый абстрактный класс для продуктов """

    @abstractmethod
    def check_minimum_stock(self):
        """ Проверка наличия на складе остатка меньше количества 10 штук """
        pass


class Product(AbstractProduct, ReprMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
         :name название
         :description описание
         :price цена
         :quantity количество в наличии
         """
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    # def __str__(self):
        # return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
        # return f"{self.name},{self.description}, {self.__price}, {self.quantity}."


    def __add__(self, other):
        """Результат сложения двух продуктов, умноженных на количество на складе"""
        # if not isinstance(other, self.__class__):
        if not type(self) is type(other):
            raise TypeError("Нельзя складывать товары разных типов")
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

    def check_minimum_stock(self):
        if self.quantity < 10:
            print(f"Внимание! Товар {self.name} на складе осталось меньше 10 единиц.")


class Smartphone(Product, ReprMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: str, model: str, memory: int, color: str):
        """
        :name название
        :description описание
        :price цена
        :quantity количество в наличии
        :performance производительность
        :model модель
        :memory объем встроенной памяти
        :color цвет
        """
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def check_minimum_stock(self):
        if self.quantity < 10:
            print(f"Внимание! Товар {self.name} на складе осталось меньше 10 единиц.")


class LawnGrass(Product, ReprMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 manufacturer_country: str, germination_period: int, color: str):
        """
        :name название
        :description описание
        :price цена
        :quantity количество в наличии
        :manufacturer_country страна-производитель
        :germination_period срок прорастания
        :color цвет
        """
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color

    def check_minimum_stock(self):
        if self.quantity < 10:
            print(f"Внимание! Товар {self.name} на складе осталось меньше 10 единиц.")
