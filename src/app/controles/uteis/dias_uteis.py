import numpy as np
import pandas as pd


def calcular_dias_uteis(ano: int, feriados: list[str]) -> np.ndarray:
    # mes:02d - formata um numero inteiro de um digito para dois - Ex: 1 para 01, 6 para 06
    lista_primeiro_dia_de_cada_mes = [f"{ano}-{mes:02d}-01" for mes in range(1, 13)]
    lista_ultimo_dia_de_cada_mes = [
        (pd.Timestamp(data) + pd.DateOffset(months=1, days=-1)).strftime("%Y-%m-%d")
        for data in lista_primeiro_dia_de_cada_mes
    ]
    return np.busday_count(lista_primeiro_dia_de_cada_mes, lista_ultimo_dia_de_cada_mes, holidays=feriados)
