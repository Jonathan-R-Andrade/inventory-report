from inventory_report.importer.importer import Importer
from inventory_report.inventory.product import Product
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str) -> list[Product]:
        file_type = file_path.split(".")[-1]
        if file_type.lower() != "xml":
            raise ValueError("Arquivo inválido")
        with open(file_path, mode="r") as file:
            data = xmltodict.parse(file.read())["dataset"]["record"]
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
