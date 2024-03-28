from src.product import Product


class Category:
    """
    :total_categories всего категорий
    :total_unique_products всего уникальные продукты
    """
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products):
        """
        :name название
        :description описание
        :products товары
        """
        self.name = name
        self.description = description
        self.__products = products
        self.total_categories += 1
        self.total_unique_products += len(products)

    def __len__(self) -> int:
        return sum(products.quantity for products in self.__products)
        # return len(self.__products)

    def __str__(self) -> str:
        # Название категории, количество продуктов: 200 шт.
        return f"{self.name}, количество продуктов: {self.__len__()} шт."

    def __add__(self, other):
        if isinstance(other, Category):
            return Category(self.name + other.name, self.description + other.description, self.__products + other.__products)
        elif isinstance(other, Product):
            return Category(self.name, self.description, self.__products + [other])
        else:
            raise TypeError("Неверный тип")



    @property
    def product(self):
        """"Возвращает список продуктов"""
        product_list = []
        for product in self.__products:
            product_list.append({"name": product.name,
                                 "description": product.description,
                                 "price": product.price,
                                 "quantity": product.quantity})

        return product_list

    @product.setter
    def product(self, product: Product):
        """
        Добавляет продукт в категорию
        :product экземпляр класса Product
        """
        self.__products.append(product)
        self.total_unique_products += 1

    @property
    def products_format(self) -> list[str]:
        """Возвращает список продуктов в формате"""
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return product_list
