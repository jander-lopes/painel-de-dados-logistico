import pandas as pd

DataFrame = pd.DataFrame


def transformar(dados: DataFrame) -> DataFrame:
    dados["data"] = pd.to_datetime(dados["data"], format='%d/%m/%Y')
    return dados
