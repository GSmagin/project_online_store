class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):
        while self.index < len(self.category):
            # product = self.category[self.index].get("name")
            product = self.category[self.index]
            self.index += 1
            return product
        raise StopIteration



