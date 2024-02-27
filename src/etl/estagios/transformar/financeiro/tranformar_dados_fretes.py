import pandas as pd

from .coletar_dados_tabela_veiculo import dados_de_veiculos

DataFrame = pd.DataFrame


def fretes(dados: list[DataFrame]) -> DataFrame:
    fretes, veiculos = dados
    juntar_veiculos = dados_de_veiculos(fretes, veiculos)
    destinos = __tratar_coluna_destino(juntar_veiculos)
    ano_mes = __criar_colunas_ano_e_num_mes(destinos)
    df = __agrupar_dados_frete(ano_mes)
    df.columns = ["ano", "num_mes", "mes", "filial", "tipo_veiculo", "carroceria", "qnt_pedidos", "receitas"]
    df["receitas"] = df["receitas"].round(2)
    return df


def __criar_colunas_ano_e_num_mes(dados: DataFrame) -> DataFrame:
    datas = pd.to_datetime(dados["DataPedido"], format="%d/%m/%Y")
    dados["ano"] = datas.dt.year
    dados["num_mes"] = datas.dt.month
    dados["mes"] = datas.dt.month_name(locale="pt_BR")
    return dados.copy()


def __tratar_coluna_destino(dados: DataFrame) -> DataFrame:
    destinos = dados["Destino"].str.split("/|\\*", expand=True)
    destinos.columns = ["regiao", "estado", "cidade"]
    return pd.concat([dados, destinos], axis=1).drop("Destino", axis=1)


def __agrupar_dados_frete(dados: DataFrame) -> DataFrame:
    agregar = dict(NroPedido="count", ValorFrete="sum")
    return dados.groupby(["ano", "num_mes", "mes", "Filial", "TipoVeiculo", "Carroceria"]).agg(agregar).reset_index()
