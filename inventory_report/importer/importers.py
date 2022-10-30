from typing import Dict
from inventory_report.importer.importer import Importer
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter

importers: Dict[str, Importer] = {
    "json": JsonImporter,
    "csv": CsvImporter,
    "xml": XmlImporter,
}
