import streamlit
from streamlit_autorefresh import st_autorefresh

import src.congifuracao.variaveis as var

from .visualizacoes.pagina_financeiro import financeiro


def iniciar_aplicativo(st: streamlit):
    financeiro(st)
    st_autorefresh(interval=var.TEMPO_ATUALIZACAO_DA_PAGINA)
