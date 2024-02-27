from pathlib import Path


def renomear_e_mover_arquivo(arquivo: Path, mover_para: Path):
    arquivo.rename(mover_para)
