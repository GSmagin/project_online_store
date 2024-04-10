class CategoryIterator:
    """Iterator for categories"""
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < len(self.category.product):
            # product = self.category[self.index].get("name")
            result = self.category.product[self.index]
            self.index += 1
            return result
            # return result.get("name")
        else:
            raise StopIteration



