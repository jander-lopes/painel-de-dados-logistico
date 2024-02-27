import datetime as dt
from dataclasses import dataclass
from pathlib import Path

import src.congifuracao.diretorios as diretorio


@dataclass
class DadosEstagioExtracao:
    pasta: str
    nome_arquivo: str
    linha_cabecalho: int = 0

    def __post_init__(self) -> None:
        data = dt.datetime.now()
        data_backup = data.isoformat("T", "seconds").replace(":", "-")
        self.arquivo_bd = self.__definir_caminho_do_arquivo_no_bd(data)
        self.arquivo = diretorio.EXTRACAO_PASTA_DADOS / f"{self.nome_arquivo}.parquet"
        self.backup = diretorio.EXTRACAO_PASTA_BACKUP / f"{self.nome_arquivo}_{data_backup}.parquet"

    def __definir_caminho_do_arquivo_no_bd(self, data: dt.datetime) -> Path:
        caminho = diretorio.BD_RELATORIOS / self.pasta
        if self.pasta in ["metas", "feriados"]:
            return caminho / f"{self.nome_arquivo}.csv"
        if self.pasta in ["fretes", "custos"]:
            caminho = caminho / str(data.year)
        return caminho / f"{self.nome_arquivo}_{data.month}_{data.year}.csv"
