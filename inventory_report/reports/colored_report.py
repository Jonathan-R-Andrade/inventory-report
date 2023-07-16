from inventory_report.inventory.product import Product
from inventory_report.reports.report import Report
import re


class ColoredReport:
    def __init__(self, report_type: Report):
        self.report_type = report_type

    def __colorize_dates(self, report: str, color_code: int) -> str:
        dates = re.findall(r"(\d+-\d+-\d+)", report)

        for date in dates:
            report = report.replace(
                date,
                f"\033[{color_code}m{date}\033[0m",
            )

        return report

    def __colorize_companies(self, report: str, color_code: int) -> str:
        companies = re.findall(r"(- .+:)", report)

        for company in companies:
            report = report.replace(
                company,
                f"- \033[{color_code}m{company[2:-1]}\033[0m:",
            )

        return report

    def __colorize_total_stocked_products(
        self, report: str, color_code: int
    ) -> str:
        total_stocked_products = re.findall(r"(: \d+)", report)

        for stocked_product in total_stocked_products:
            report = report.replace(
                stocked_product,
                f": \033[{color_code}m{stocked_product[2:]}\033[0m",
            )

        return report

    def generate(self, products_list: list[Product]) -> str:
        report = self.report_type.generate(products_list)
        index_start = report.find("mais produtos:") + 15
        index_finish = report.find("\n", index_start)
        if index_finish == -1:
            index_finish = len(report)

        report = (
            report[:index_start]
            + "\033[31m"
            + report[index_start:index_finish]
            + "\033[0m"
            + report[index_finish:]
        )

        green_phrases = [
            "Data de fabricação mais antiga:",
            "Data de validade mais próxima:",
            "Empresa com mais produtos:",
            "Produtos estocados por empresa:",
        ]

        for phrase in green_phrases:
            report = report.replace(
                phrase,
                f"\033[32m{phrase}\033[0m",
            )

        report = self.__colorize_dates(report, 36)
        report = self.__colorize_companies(report, 31)
        report = self.__colorize_total_stocked_products(report, 34)

        return report
