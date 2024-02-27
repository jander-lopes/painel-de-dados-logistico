from enum import Enum

import numpy as np
from pandas import Series


class StatusMeta(Enum):
    ACIMA = "ACIMA"
    ABAIXO = "ABAIXO"
    NEUTRO = "NEUTRO"


def indicador_acima_ou_abaixo_meta(realizado: Series, metas: Series) -> np.ndarray:
    return np.where(realizado > metas, StatusMeta.ACIMA.value, StatusMeta.ABAIXO.value)


def indicador_acima_ou_abaixo_limite_custo() -> np.ndarray:
    return 1
