import pandas as pd

DataFrame = pd.DataFrame


def dados_de_veiculos(tabela: DataFrame, veiculos: DataFrame) -> DataFrame:
    return pd.merge(tabela, veiculos, how="left", on="ID_Veiculo")
