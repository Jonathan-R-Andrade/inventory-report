import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            products = [row for row in reader]
        if report_type == "simples":
            return SimpleReport.generate(products)
        return CompleteReport.generate(products)
