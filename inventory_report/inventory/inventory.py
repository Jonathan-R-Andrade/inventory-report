import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path, mode="r") as file:
            file_type = file_path.split(".")[-1]
            products = []
            if file_type.lower() == "csv":
                reader = csv.DictReader(file)
                products = [row for row in reader]
            elif file_type.lower() == "json":
                products = json.load(file)
            elif file_type.lower() == "xml":
                products = xmltodict.parse(file.read())["dataset"]["record"]

        if report_type == "simples":
            return SimpleReport.generate(products)
        return CompleteReport.generate(products)
