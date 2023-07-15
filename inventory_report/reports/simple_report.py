from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products):
        def sort_dates(iso_format_date):
            date = datetime.fromisoformat(iso_format_date)
            return datetime.toordinal(date)

        manufacturing_dates = [
            product["data_de_fabricacao"] for product in products
        ]
        manufacturing_dates.sort(key=sort_dates)

        expiration_dates = [
            product["data_de_validade"]
            for product in products
            if datetime.fromisoformat(product["data_de_validade"])
            > datetime.now()
        ]
        expiration_dates.sort(key=sort_dates)

        companies = [product["nome_da_empresa"] for product in products]
        company_with_more_products, _ = Counter(companies).most_common(1)[0]

        return (
            f"Data de fabricação mais antiga: {manufacturing_dates[0]}"
            f"\nData de validade mais próxima: {expiration_dates[0]}"
            f"\nEmpresa com mais produtos: {company_with_more_products}\n"
        )
