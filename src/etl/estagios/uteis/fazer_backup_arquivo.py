from pathlib import Path

from .coletar_arquivo import coletar_arquivos
from .deletar_arquivo import deletar_arquivo
from .listar_arquivos import listar_arquivos
from .renomear_e_mover_arquivo import renomear_e_mover_arquivo


def fazer_backup(arquivo: Path, arquivo_backup: Path, dir_backup: Path, nome_arquivo: str):
    if arquivo.is_file():
        arquivos = listar_arquivos(dir_backup, "parquet")
        arquivos_para_deletar = coletar_arquivos(nome_arquivo, arquivos)
        renomear_e_mover_arquivo(arquivo, arquivo_backup)
        if arquivo_backup.is_file():
            deletar_arquivo(arquivos_para_deletar)
