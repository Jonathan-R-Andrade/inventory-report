from abc import ABC, abstractmethod
from inventory_report.inventory.product import Product


class Report(ABC):
    @classmethod
    @abstractmethod
    def generate(cls, products: list[Product]) -> str:
        raise NotImplementedError
