import os

from dotenv import load_dotenv

load_dotenv()

# Tempos em segundos
TEMPO_ATUALIZACAO_ETL = int(os.getenv("TEMPO_ATUALIZACAO_ETL"))
TEMPO_CACHE_DADOS = int(os.getenv("TEMPO_CACHE_DADOS"))

# Tempos em milisegundos
# 1_000 = 1 segundo
TEMPO_ATUALIZACAO_DA_PAGINA = int(os.getenv("TEMPO_ATUALIZACAO_DA_PAGINA")) * 1_000

CUSTOS_SOBRE_RECEITA = float(os.getenv("LIMITE_DE_CUSTO")) / 100
