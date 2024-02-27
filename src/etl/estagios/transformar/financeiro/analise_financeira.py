import datetime as dt

import pandas as pd

import src.congifuracao.diretorios as diretorio

from ...uteis.fazer_backup_arquivo import fazer_backup
from ..uteis.carregar_dados import carregar_dados
from .tranformar_dados_fretes import fretes
from .transformar_dados_custos import custos

DataFrame = pd.DataFrame

__arquivos = ["relatorio_cargas", "custos_mensais", "cadastro_veiculo"]
__colunas = [
    ["NroPedido", "Destino", "DataPedido", "ID_Veiculo", "ValorFrete"],
    None,
    ["ID_Veiculo", "Carroceria", "TipoVeiculo", "Filial"],
]


def dados_para_analise_financeira() -> DataFrame:
    data = dt.datetime.now().isoformat("T", "seconds").replace(":", "-")
    arquivo = diretorio.TRANSFORMAR_PASTA_DADOS / "dados_analise_financeira.parquet"
    backup = diretorio.TRANSFORMAR_PASTA_BACKUP / f"dados_analise_financeira-{data}.parquet"
    dados_fretes, dados_custos, dados_veiculos = carregar_dados(__arquivos, __colunas)
    df_fretes = fretes([dados_fretes, dados_veiculos])
    df_custos = custos([dados_custos, dados_veiculos])
    df = pd.merge(df_fretes, df_custos, how="left", on=["ano", "num_mes", "filial", "tipo_veiculo", "carroceria"])
    fazer_backup(arquivo, backup, diretorio.TRANSFORMAR_PASTA_BACKUP, arquivo.stem)
    df.to_parquet(arquivo)
    print(f"Transformar: {arquivo.name} -> OK -> Data: {dt.datetime.now()}")
