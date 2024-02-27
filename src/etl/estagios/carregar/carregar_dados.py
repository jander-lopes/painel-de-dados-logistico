import datetime as dt
import shutil

import src.congifuracao.diretorios as diretorio

from ..uteis.fazer_backup_arquivo import fazer_backup
from .dados_para_carregar import dados_de_carregar


def estagio_carregar() -> None:
    print("\nEstágio Carregar Inicilizado\n")
    dados = dados_de_carregar()
    for dado in dados:
        if dado.dir_dados.is_file():
            fazer_backup(dado.dir_dados, dado.dir_backup, diretorio.BANCO_DE_DADOS_BACKUP, dado.dir_dados.stem)
        if dado.dir_transformacao.is_file():
            shutil.copy2(dado.dir_transformacao, dado.dir_dados)
        print(f"Carregar: {dado.dir_dados.name} -> OK -> Data: {dt.datetime.now()}")
    print("\nEstágio Carregar Finalizado\n")
