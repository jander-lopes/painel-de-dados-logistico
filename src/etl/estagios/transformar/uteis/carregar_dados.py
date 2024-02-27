import pandas as pd

import src.congifuracao.diretorios as diretorio

DataFrame = pd.DataFrame


def carregar_dados(arquivos: list[str], colunas: list[str | None]) -> list[DataFrame]:
    dados = []
    for arquivo, colunas in zip(arquivos, colunas):
        df = pd.read_parquet(diretorio.EXTRACAO_PASTA_DADOS / f"{arquivo}.parquet", columns=colunas)
        dados.append(df)
    return dados
