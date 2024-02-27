import datetime as dt

from pandas import DataFrame

import src.congifuracao.diretorios as diretorio

from ...uteis.fazer_backup_arquivo import fazer_backup
from ..uteis.carregar_dados import carregar_dados
from .transformar import transformar

__arquivos = ["metas"]
__colunas = [None]


def dados_metas() -> DataFrame:
    data = dt.datetime.now().isoformat("T", "seconds").replace(":", "-")
    arquivo = diretorio.TRANSFORMAR_PASTA_DADOS / "metas.parquet"
    backup = diretorio.TRANSFORMAR_PASTA_BACKUP / f"metas-{data}.parquet"
    metas = carregar_dados(__arquivos, __colunas)[0]
    df = transformar(metas)
    fazer_backup(arquivo, backup, diretorio.TRANSFORMAR_PASTA_BACKUP, arquivo.stem)
    df.to_parquet(arquivo, index=False)
    print(f"Transformar: {arquivo.name} -> OK -> Data: {dt.datetime.now()}")
