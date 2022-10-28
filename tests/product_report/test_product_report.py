from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_relatorio_produto():
    pf = ProductFactory()
    product = Product(
        pf.id,
        pf.nome_do_produto,
        pf.nome_da_empresa,
        pf.data_de_fabricacao,
        pf.data_de_validade,
        pf.numero_de_serie,
        pf.instrucoes_de_armazenamento,
    )

    expected_phrase = (
        f"O produto {pf.nome_do_produto}"
        f" fabricado em {pf.data_de_fabricacao}"
        f" por {pf.nome_da_empresa} com validade"
        f" até {pf.data_de_validade}"
        f" precisa ser armazenado {pf.instrucoes_de_armazenamento}."
    )

    assert str(product) == expected_phrase
