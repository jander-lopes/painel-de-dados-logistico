from plotly.graph_objects import Figure

import src.app.configuracao.cores as cor
from src.app.controles.financeiro.custos_por_tipo_veiculo import ControleDadosSaida, controle
from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.visualizacoes.uteis.configurar_grafico import configurar_grafico_barras

from ..uteis.nomes_dos_graficos import NomeGraficos
from .metodos import dados_grafico, grafico


def desenhar(requisicao: DadosRequisicao) -> Figure:
    dados_entrada = controle(requisicao)
    graficos = __graficos(dados_entrada)
    fig = Figure().add_traces(graficos)
    __configuracoes(fig)
    return fig


def __graficos(dados: ControleDadosSaida) -> list:
    return [
        grafico(dados, dados_grafico(dados, NomeGraficos.ABASTECIMENTO, cor.abastecimento)),
        grafico(dados, dados_grafico(dados, NomeGraficos.MANUTENCAO, cor.manutencao)),
        grafico(dados, dados_grafico(dados, NomeGraficos.CUSTOS_FIXOS, cor.custos_fixos)),
    ]


def __configuracoes(fig: Figure) -> None:
    configurar_grafico_barras(fig)
    fig.update_layout(barmode="stack")
    fig.update_traces(width=0.5)
