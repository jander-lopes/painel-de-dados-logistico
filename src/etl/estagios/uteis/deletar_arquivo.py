from pathlib import Path


def deletar_arquivo(arquivos: list[Path]):
    [arquivo.unlink() for arquivo in arquivos]
