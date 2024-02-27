import plotly.graph_objects as go
from pandas import Series

from .modelo_dados import GraficoDadosEntrada


def linha(
    entrada: GraficoDadosEntrada,
    cores: str | Series,
    dados_customizados: tuple[Series],
    dica_ferramenta: str,
) -> go.Scatter:
    return go.Scatter(
        name=entrada.nome.value,
        x=entrada.eixo_x,
        y=entrada.eixo_y,
        marker_color=cores,
        line=dict(dash="dot"),
        customdata=dados_customizados,
        hovertemplate=dica_ferramenta,
        xaxis=entrada.xaxis,
    )
