import numpy as np
import plotly.graph_objects as go
from pandas import Series

from .modelo_dados import GraficoDadosEntrada


def colunas(
    entrada: GraficoDadosEntrada,
    rotulo_dados: Series,
    cores: str | Series,
    dados_customizados: tuple[Series],
    dica_ferramenta: str,
    orientacao: str | None = None,
    posicao_rotulo: str = "auto",
) -> go.Bar:
    custom_data = np.stack(dados_customizados, axis=-1) if dados_customizados else None
    return go.Bar(
        name=entrada.nome.value,
        x=entrada.eixo_x,
        y=entrada.eixo_y,
        text=rotulo_dados,
        textposition=posicao_rotulo,
        orientation=orientacao,
        marker_color=cores,
        customdata=custom_data,
        hovertemplate=dica_ferramenta,
    )
