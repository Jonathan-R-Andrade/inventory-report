from typing import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item
