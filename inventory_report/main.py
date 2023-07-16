import sys
from inventory_report.importer.importers import importers
from inventory_report.inventory.inventory import Inventory


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return 1
    file_type = sys.argv[1].split(".")[-1].lower()
    importer = importers[file_type]
    inventory = Inventory(importer)
    report = inventory.import_data(sys.argv[1], sys.argv[2])
    print(report, end="")
    return 0
