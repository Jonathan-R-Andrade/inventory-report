from abc import ABC, abstractmethod
from inventory_report.inventory.product import Product


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls, file_path) -> list[Product]:
        raise NotImplementedError
