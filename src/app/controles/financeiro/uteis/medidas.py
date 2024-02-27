import numpy as np
from pandas import Series

Numero = np.float64 | np.int64


def resultado(receitas: Series | Numero, custos: Series | Numero) -> Series | Numero:
    return receitas - custos


def margem(resultados: Series | Numero, receitas: Series | Numero) -> Series | Numero:
    return (resultados / receitas) * 100


def ticket_medio(receitas: Series, qnt_pedidos: Series) -> Series:
    return receitas / qnt_pedidos
