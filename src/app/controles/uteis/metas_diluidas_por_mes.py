def calcular_metas_diluida_mes(dias_uteis: list[int], meta_ano: int | float) -> None:
    dias_uteis_ano = sum(dias_uteis)
    metas = (dias_uteis / dias_uteis_ano) * meta_ano
    return [int(valor) for valor in metas]
