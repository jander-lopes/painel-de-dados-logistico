from dataclasses import dataclass
from pathlib import Path


@dataclass
class DadosEstagioCarregar:
    dir_transformacao: Path
    dir_dados: Path
    dir_backup: Path
