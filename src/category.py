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


    @property
    def product(self):
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
        :param product: экземпляр класса Product
        """
        self.__products.append(product)
        self.total_unique_products += 1









