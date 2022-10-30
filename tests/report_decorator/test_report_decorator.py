import re
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.colored_report import ColoredReport

PRODUCTS = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-12-06",
        "data_de_validade": "2023-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
]


def test_decorar_relatorio():
    simple_report = ColoredReport(SimpleReport).generate(PRODUCTS)
    complete_report = ColoredReport(CompleteReport).generate(PRODUCTS)

    expected = (
        "^\\033\\[32mData de fabricação mais antiga:\\033\\[0m "
        "\\033\\[36m2020-12-06\\033\\[0m\\n"
        "\\033\\[32mData de validade mais próxima:\\033\\[0m "
        "\\033\\[36m2023-09-17\\033\\[0m\\n"
        "\\033\\[32mEmpresa com mais produtos:\\033\\[0m "
        "\\033\\[31mTarget Corporation\\033\\[0m"
    )
    simple_report_match = re.search(expected, simple_report)
    complete_report_match = re.search(expected, complete_report)

    assert bool(simple_report_match)
    assert bool(complete_report_match)
