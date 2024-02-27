import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BD_RELATORIOS = Path(os.getenv("BD_RELATORIOS"))

BANCO_DE_DADOS = Path(os.getenv("BANCO_DE_DADOS"))
BANCO_DE_DADOS_BACKUP = Path(os.getenv("BANCO_DE_DADOS_BACKUP"))

# DIRETORIOS APLICATIVO STREAMLIT
ARQUIVO_ANALISE_FINANCEIRA = BANCO_DE_DADOS / "dados_analise_financeira.parquet"
ARQUIVO_METAS = BANCO_DE_DADOS / "metas.parquet"
ARQUIVO_FERIADOS = BANCO_DE_DADOS / "feriados_nacionais.parquet"

# DIRETORIOS APLICATIVO ETL
DIRETORIO_DO_PROJETO = Path()
EXTRACAO_PASTA_DADOS = DIRETORIO_DO_PROJETO / "src/etl/estagios/extracao/dados"
EXTRACAO_PASTA_BACKUP = EXTRACAO_PASTA_DADOS / "backup"

TRANSFORMAR_PASTA_DADOS = DIRETORIO_DO_PROJETO / "src/etl/estagios/transformar/dados"
TRANSFORMAR_PASTA_BACKUP = TRANSFORMAR_PASTA_DADOS / "backup"
