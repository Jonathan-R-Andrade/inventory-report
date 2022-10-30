from inventory_report.importer.importers import importers
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        file_type = file_path.split(".")[-1]
        data = importers[file_type.lower()].import_data(file_path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
        raise ValueError(
            'O parâmetro "report_type" deve ser "simples" ou "completo"'
        )
