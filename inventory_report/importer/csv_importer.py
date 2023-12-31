from inventory_report.importer.importer import Importer
from inventory_report.inventory.product import Product
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str) -> list[Product]:
        file_type = file_path.split(".")[-1]
        if file_type.lower() != "csv":
            raise ValueError("Arquivo inválido")
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            products = [
                Product(
                    row["id"],
                    row["nome_do_produto"],
                    row["nome_da_empresa"],
                    row["data_de_fabricacao"],
                    row["data_de_validade"],
                    row["numero_de_serie"],
                    row["instrucoes_de_armazenamento"],
                )
                for row in reader
            ]
        return products
