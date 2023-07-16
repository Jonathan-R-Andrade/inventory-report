from inventory_report.importer.importer import Importer
from inventory_report.inventory.product import Product
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path) -> list[Product]:
        file_type = file_path.split(".")[-1]
        if file_type.lower() != "json":
            raise ValueError("Arquivo inválido")
        with open(file_path, mode="r") as file:
            data = json.load(file)
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
                for row in data
            ]
        return products
