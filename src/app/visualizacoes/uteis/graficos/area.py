import plotly.graph_objects as go
from pandas import Series

from .modelo_dados import GraficoDadosEntrada


def area(
    entrada: GraficoDadosEntrada,
    cor_area: str | Series,
    modelo: str,
    dica_ferramenta: str,
) -> go.Scatter:
    return go.Scatter(
        name=entrada.nome.value,
        x=entrada.eixo_x,
        y=entrada.eixo_y,
        text=entrada.eixo_y,
        mode="lines+markers+text",
        texttemplate=modelo,
        textposition="top center",
        line=dict(color=entrada.cor, dash="dash"),
        fill="tozeroy",
        fillcolor=cor_area,
        cliponaxis=False,
        hovertemplate=dica_ferramenta,
    )
