import pandas as pd

from .coletar_dados_tabela_veiculo import dados_de_veiculos

DataFrame = pd.DataFrame


def custos(dados: list[DataFrame]) -> DataFrame:
    custos, veiculos = dados
    juntar_veiculos = dados_de_veiculos(custos, veiculos)
    datas = __tratar_coluna_data(juntar_veiculos)
    df = __agrupar_dados_custos(datas)
    __renomear_colunas(df)
    df.iloc[:, 5:] = df.iloc[:, 5:].round(2)
    return df


def __tratar_coluna_data(dados: pd.DataFrame) -> DataFrame:
    datas = dados["Data"].str.split("/", expand=True)
    datas.columns = ["num_mes", "ano"]
    datas = datas.astype("int")
    return pd.concat([dados, datas], axis=1).drop("Data", axis=1)


def __agrupar_dados_custos(dados: pd.DataFrame) -> DataFrame:
    agregar = dict(ValorAbastecimento="sum", ValorManutencao="sum", CustoFixo="sum", CustoTotal="sum")
    return dados.groupby(["ano", "num_mes", "Filial", "TipoVeiculo", "Carroceria"]).agg(agregar).reset_index()


def __renomear_colunas(dados: DataFrame) -> None:
    dados.columns = [
        "ano",
        "num_mes",
        "filial",
        "tipo_veiculo",
        "carroceria",
        "abastecimento",
        "manutencao",
        "custo_fixo",
        "custos",
    ]
