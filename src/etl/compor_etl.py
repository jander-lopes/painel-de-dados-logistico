import os
import time

import src.congifuracao.variaveis as var

from .estagios.carregar.carregar_dados import estagio_carregar
from .estagios.extracao.extrair_dados import estagio_extracao
from .estagios.transformar.transformar_dados import estagio_transformar


def iniciar_etl():
    try:
        while True:
            os.system("cls")
            __executar_etl()
            time.sleep(var.TEMPO_ATUALIZACAO_ETL)
    except KeyboardInterrupt:
        print("Servidor interrompido manualmente")


def __executar_etl():
    estagio_extracao()
    estagio_transformar()
    estagio_carregar()
