import pandas as pd
import streamlit as st

import src.congifuracao.diretorios as diretorio
import src.congifuracao.variaveis as var

DataFrame = pd.DataFrame


@st.cache_data(ttl=var.TEMPO_CACHE_DADOS)
def dados_analise_financeira() -> DataFrame:
    return pd.read_parquet(diretorio.ARQUIVO_ANALISE_FINANCEIRA)


@st.cache_data(ttl=var.TEMPO_CACHE_DADOS)
def tb_metas() -> DataFrame:
    return pd.read_parquet(diretorio.ARQUIVO_METAS)


@st.cache_data(ttl=var.TEMPO_CACHE_DADOS)
def tb_feriados() -> DataFrame:
    return pd.read_parquet(diretorio.ARQUIVO_FERIADOS)
