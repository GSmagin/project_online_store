class Category:
    """
    total_categories всего категорий
    :total_unique_products всего уникальные продукты
    """
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        """
        :name название
        :description описание
        :products товары
        """
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += len(products)
