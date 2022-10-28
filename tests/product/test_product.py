from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_cria_produto():
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

    assert product.id == pf.id
    assert product.nome_do_produto == pf.nome_do_produto
    assert product.nome_da_empresa == pf.nome_da_empresa
    assert product.data_de_fabricacao == pf.data_de_fabricacao
    assert product.data_de_validade == pf.data_de_validade
    assert product.numero_de_serie == pf.numero_de_serie
    assert (
        product.instrucoes_de_armazenamento == pf.instrucoes_de_armazenamento
    )
