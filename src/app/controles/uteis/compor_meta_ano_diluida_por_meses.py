import numpy as np

from src.app.controles.uteis.dias_uteis import calcular_dias_uteis
from src.app.controles.uteis.metas_diluidas_por_mes import calcular_metas_diluida_mes
from src.app.uteis.calendario import feriados_cidade_sp


def meta_ano_diluida_por_meses(ano: int, meta: float) -> np.ndarray:
    feriados_sp = feriados_cidade_sp(ano)
    dias_uteis = calcular_dias_uteis(ano, feriados_sp)
    return calcular_metas_diluida_mes(dias_uteis, meta)
