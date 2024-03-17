class FileJson:

    def __init__(self, data) -> None:
        self.name = data.get("name")
        self.description = data.get("description")
        self.products_name = data.get("products").get("name")
        self.products_description = data.get("products").get("description")
        self.products_price = data.get("products").get("price")
        self.products_quantity = data.get("products").get("quantity")
