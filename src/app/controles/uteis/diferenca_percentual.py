from pandas import Series


def diferenca_percentual(valor_atual: Series, valor_comparar: Series) -> Series:
    return ((valor_atual - valor_comparar) / abs(valor_comparar)) * 100
