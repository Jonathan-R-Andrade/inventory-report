from typing import Iterable
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.colored_report import ColoredReport


class Inventory(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_path: str, report_type: str):
        self.data.extend(self.importer.import_data(file_path))
        if report_type == "simples":
            return ColoredReport(SimpleReport).generate(self.data)
        elif report_type == "completo":
            return ColoredReport(CompleteReport).generate(self.data)
        raise ValueError(
            'O parâmetro "report_type" deve ser "simples" ou "completo"'
        )
