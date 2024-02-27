from pathlib import Path


def coletar_arquivos(nome_arquivo: str, arquivos: list[Path]):
    return [arquivo for arquivo in arquivos if nome_arquivo == arquivo.stem[: len(nome_arquivo)]]
