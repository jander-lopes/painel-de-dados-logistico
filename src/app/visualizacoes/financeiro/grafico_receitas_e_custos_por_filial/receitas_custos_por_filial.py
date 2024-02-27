from plotly.graph_objects import Figure

from src.app.controles.financeiro.receitas_e_custos_por_filial import ControleDadosSaida, controle
from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.visualizacoes.uteis.configurar_grafico import configurar_grafico_barras

from .metodos import dados_custos, dados_receitas, grafico


def desenhar(requisicao: DadosRequisicao) -> Figure:
    dados_entrada = controle(requisicao)
    graficos = __graficos(dados_entrada)
    fig = Figure().add_traces(graficos)
    configurar_grafico_barras(fig)
    return fig


def __graficos(dados_entrada: ControleDadosSaida) -> list:
    return [
        grafico(dados_entrada, dados_custos(dados_entrada)),
        grafico(dados_entrada, dados_receitas(dados_entrada)),
    ]
