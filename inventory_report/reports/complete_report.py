from collections import Counter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.product import Product


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list[Product]) -> str:
        report = super().generate(products)
        companies = [product.nome_da_empresa for product in products]
        products_by_companies = Counter(companies).items()
        list_of_products_by_companies = [
            f"- {company}: {total_product}\n"
            for company, total_product in products_by_companies
        ]
        report_of_products_by_companies = "".join(
            list_of_products_by_companies
        )
        return (
            f"{report}\n"
            f"Produtos estocados por empresa:\n"
            f"{report_of_products_by_companies}"
        )
