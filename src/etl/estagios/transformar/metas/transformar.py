from pandas import DataFrame


def transformar(dados: DataFrame) -> DataFrame:
    dados["metas_receitas"] = dados["metas_receitas"].str.replace(".", "").str.replace(",", ".").astype("float")
    return dados
