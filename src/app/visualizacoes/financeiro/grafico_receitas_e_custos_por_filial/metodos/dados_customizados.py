from pandas import Series

from src.app.controles.financeiro.receitas_e_custos_por_filial import ControleDadosSaida
from src.app.uteis.formatar_unidades import formatar_valores_monetarios

from ...uteis.nomes_dos_graficos import NomeGraficos
from .dica_ferramenta import dica_limite_de_custos


def dados_customizados(dados_controle: ControleDadosSaida, nome_grafico: NomeGraficos) -> tuple[Series]:
    valor_dica_ferramenta = dados_controle.receitas
    if nome_grafico == NomeGraficos.RECEITA:
        valor_dica_ferramenta = dados_controle.custos
    return (
        formatar_valores_monetarios(valor_dica_ferramenta, 0),
        formatar_valores_monetarios(dados_controle.resultados, 0),
        dica_limite_de_custos(dados_controle.taxa_limite_custos),
    )
