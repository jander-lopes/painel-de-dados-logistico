from plotly.graph_objects import Figure

import src.app.configuracao.cores as cor
from src.app.controles.financeiro.modelo_dados import ControleDadosSaida
from src.app.controles.financeiro.receitas_meses import controle
from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.visualizacoes.uteis.configurar_grafico import configurar_grafico_colunas

from ..uteis.nomes_dos_graficos import NomeGraficos
from .metodos import dados_barra, dados_linha, graf_barra, graf_linha


def desenhar(requisicao: DadosRequisicao) -> Figure:
    dados_entrada = controle(requisicao)
    graficos = __graficos(dados_entrada)
    fig = Figure().add_traces(graficos)
    configurar_grafico_colunas(fig)
    return fig


def __graficos(dados: ControleDadosSaida) -> list:
    return [
        graf_barra(dados, dados_barra(dados, NomeGraficos.RECEITA, cor.receitas, cor.abaixo_meta)),
        graf_linha(dados, dados_linha(dados, NomeGraficos.META, cor.meta_receitas)),
    ]
