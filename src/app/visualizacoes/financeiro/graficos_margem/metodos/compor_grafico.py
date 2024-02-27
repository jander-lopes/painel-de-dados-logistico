from typing import Callable

from plotly.graph_objects import Figure, Scatter

from src.app.controles.financeiro.margem_meses import ControleDadosSaida
from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.visualizacoes.uteis.configurar_grafico import configuracao_grafico_margem

from . import dados_graf, grafico


def compor_grafico(controle: Callable, requisicao: DadosRequisicao | None = None) -> Figure:
    dados_entrada = controle(requisicao) if requisicao else controle()
    grafico = __grafico(dados_entrada)
    fig = Figure().add_traces(grafico)
    configuracao_grafico_margem(fig, len(dados_entrada.eixo_x))
    return fig


def __grafico(dados_entrada: ControleDadosSaida) -> Scatter:
    return grafico(dados_graf(dados_entrada))
