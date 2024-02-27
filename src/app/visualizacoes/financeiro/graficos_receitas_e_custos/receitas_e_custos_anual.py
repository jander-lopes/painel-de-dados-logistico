from plotly.graph_objects import Figure

import src.app.configuracao.cores as cor
from src.app.controles.financeiro.modelo_dados import ControleDadosSaida
from src.app.controles.financeiro.receitas_e_custos_anual import controle
from src.app.visualizacoes.uteis.configurar_grafico import configurar_grafico_colunas

from ..uteis.nomes_dos_graficos import NomeGraficos
from .metodos import dados_barra, dados_linha, graf_barra, graf_linha


def desenhar() -> Figure:
    dados_entrada = controle()
    graficos = __graficos(dados_entrada)
    fig = Figure().add_traces(graficos)
    __configuracoes(fig)
    return fig


def __graficos(dados_entrada: ControleDadosSaida) -> list:
    receitas, custos = dados_entrada
    return [
        graf_barra(receitas, dados_barra(receitas, NomeGraficos.RECEITA, cor.receitas, cor.abaixo_meta)),
        graf_barra(custos, dados_barra(custos, NomeGraficos.CUSTO, cor.limite_de_custo, cor.custos)),
        graf_linha(receitas, dados_linha(receitas, NomeGraficos.META, cor.meta_receitas, "x3")),
        graf_linha(custos, dados_linha(custos, NomeGraficos.LIMITE_CUSTO, cor.meta_custos, "x4")),
    ]


def __configuracoes(fig: Figure) -> None:
    fig.update_layout(
        xaxis3=dict(overlaying="x", range=[2020 - 0.3, 2024 + 0.7], showticklabels=False),
        xaxis4=dict(overlaying="x", range=[2020 - 0.7, 2024 + 0.3], showticklabels=False),
    )
    configurar_grafico_colunas(fig)
