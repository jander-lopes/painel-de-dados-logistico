import datetime as dt

import src.congifuracao.diretorios as diretorio

from ..modelo_dados.dados_carregar import DadosEstagioCarregar


def dados_de_carregar() -> list[DadosEstagioCarregar]:
    data = dt.datetime.now().isoformat("T", "seconds").replace(":", "-")
    return [
        DadosEstagioCarregar(
            diretorio.TRANSFORMAR_PASTA_DADOS / "dados_analise_financeira.parquet",
            diretorio.BANCO_DE_DADOS / "dados_analise_financeira.parquet",
            diretorio.BANCO_DE_DADOS_BACKUP / f"dados_analise_financeira-{data}.parquet",
        ),
        DadosEstagioCarregar(
            diretorio.TRANSFORMAR_PASTA_DADOS / "metas.parquet",
            diretorio.BANCO_DE_DADOS / "metas.parquet",
            diretorio.BANCO_DE_DADOS_BACKUP / f"metas-{data}.parquet",
        ),
        DadosEstagioCarregar(
            diretorio.TRANSFORMAR_PASTA_DADOS / "feriados_nacionais.parquet",
            diretorio.BANCO_DE_DADOS / "feriados_nacionais.parquet",
            diretorio.BANCO_DE_DADOS_BACKUP / f"feriados_nacionais-{data}.parquet",
        ),
    ]
