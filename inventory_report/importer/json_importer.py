from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        file_type = file_path.split(".")[-1]
        if file_type.lower() != "json":
            raise ValueError("Arquivo inválido")
        with open(file_path, mode="r") as file:
            data = json.load(file)
        return data
