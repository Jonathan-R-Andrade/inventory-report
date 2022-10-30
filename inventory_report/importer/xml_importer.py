from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        file_type = file_path.split(".")[-1]
        if file_type.lower() != "xml":
            raise ValueError("Arquivo inválido")
        with open(file_path, mode="r") as file:
            data = xmltodict.parse(file.read())["dataset"]["record"]
        return data
