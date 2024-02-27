from enum import Enum

from pandas import Series


class Indicador(Enum):
    ACIMA = "ACIMA"
    ABAIXO = "ABAIXO"


def estilizar_cor_grafico_barras(cor: str, cor_alerta: str | None = None, valores: Series | None = None) -> Series:
    if cor_alerta:
        return valores.apply(lambda indicador: __definir_cor(indicador, cor, cor_alerta))
    return cor


def __definir_cor(indicador: Series, cor: str, cor_alerta: str):
    match indicador:
        case Indicador.ACIMA.value:
            return cor
        case Indicador.ABAIXO.value:
            return cor_alerta
        case _:
            return cor
