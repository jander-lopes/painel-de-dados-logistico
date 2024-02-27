from plotly.graph_objects import Figure

from src.app.controles.financeiro.margem_anual import controle

from .metodos.compor_grafico import compor_grafico


def desenhar() -> Figure:
    return compor_grafico(controle)
