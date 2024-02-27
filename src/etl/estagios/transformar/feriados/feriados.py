import datetime as dt

from pandas import DataFrame

import src.congifuracao.diretorios as diretorio

from ...uteis.fazer_backup_arquivo import fazer_backup
from ..uteis.carregar_dados import carregar_dados
from .transformar import transformar

__arquivos = ["feriados_nacionais"]
__colunas = [None]


def dados_feriados() -> DataFrame:
    data = dt.datetime.now().isoformat("T", "seconds").replace(":", "-")
    arquivo = diretorio.TRANSFORMAR_PASTA_DADOS / "feriados_nacionais.parquet"
    backup = diretorio.TRANSFORMAR_PASTA_BACKUP / f"feriados_nacionais-{data}.parquet"
    feriados = carregar_dados(__arquivos, __colunas)[0]
    df = transformar(feriados)
    fazer_backup(arquivo, backup, diretorio.TRANSFORMAR_PASTA_BACKUP, arquivo.stem)
    df.to_parquet(arquivo)
    print(f"Transformar: {arquivo.name} -> OK -> Data: {dt.datetime.now()}")
