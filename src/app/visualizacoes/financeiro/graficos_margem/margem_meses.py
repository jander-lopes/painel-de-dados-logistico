from plotly.graph_objects import Figure

from src.app.controles.financeiro.margem_meses import controle
from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .metodos.compor_grafico import compor_grafico


def desenhar(requisicao: DadosRequisicao) -> Figure:
    return compor_grafico(controle, requisicao)
