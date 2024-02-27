from pathlib import Path


def listar_arquivos(diretorio: Path, extensao: str) -> list:
    return list(diretorio.glob(f"**/*{extensao}"))
