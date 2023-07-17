from typing import Iterator
from inventory_report.inventory.product import Product


class InventoryIterator(Iterator):
    def __init__(self, data: list[Product]):
        self.data = data
        self.index = 0

    def __next__(self) -> Product:
        if self.index == len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item
