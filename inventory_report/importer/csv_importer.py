from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        file_type = file_path.split(".")[-1]
        if file_type.lower() != "csv":
            raise ValueError("Arquivo inválido")
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
