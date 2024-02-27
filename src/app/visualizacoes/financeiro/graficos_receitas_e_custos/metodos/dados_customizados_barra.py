from pandas import Series

from src.app.controles.financeiro.modelo_dados import ControleDadosSaida
from src.app.uteis.formatar_unidades import formatar_valores_monetarios

from ...uteis.nomes_dos_graficos import NomeGraficos
from .taxa_cumprimento_meta import taxa_cumprimento_meta_custos, taxa_cumprimento_meta_receitas


def dados_customizados(dados_controle: ControleDadosSaida, nome_grafico: NomeGraficos) -> tuple[Series]:
    taxa_meta = __fluxo_taxa_cumprimento_meta(nome_grafico)
    return (
        formatar_valores_monetarios(dados_controle.eixo_y, 2),
        formatar_valores_monetarios(dados_controle.metas, 2),
        taxa_meta(dados_controle.taxas_cumprimento_meta, 1),
    )


def __fluxo_taxa_cumprimento_meta(nome_grafico: str):
    if nome_grafico == NomeGraficos.RECEITA:
        return taxa_cumprimento_meta_receitas
    return taxa_cumprimento_meta_custos
