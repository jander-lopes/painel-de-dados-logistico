from dataclasses import dataclass

from pandas import Series


@dataclass
class ControleDadosSaida:
    eixo_x: Series
    eixo_y: Series
    metas: Series | None = None
    indicadores: Series | None = None
    taxas_cumprimento_meta: Series | None = None
