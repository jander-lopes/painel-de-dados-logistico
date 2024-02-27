import streamlit as streamlit

from src.app.visualizacoes.uteis.opcoes_caixas_texto import opcoes_anos, opcoes_filiais, opcoes_meses


def inicializar(st: streamlit):

    # VARIÁVEIS DE SESSÃO -----------------------------------------------------------------------------

    if "num_mes" not in st.session_state:
        st.session_state.num_mes = None

    # MENU LATERAL ------------------------------------------------------------------------------------

    # CAIXA DE SELEÇÃO - OPÇÕES
    if "caixa_ano" not in st.session_state:
        st.session_state.caixa_ano = opcoes_anos()

    if "filtro_ano" not in st.session_state:
        st.session_state.filtro_ano = st.session_state.caixa_ano[-1]

    if "caixa_num_mes" not in st.session_state:
        st.session_state.caixa_num_mes = opcoes_meses(st.session_state.filtro_ano)

    if "caixa_meses" not in st.session_state:
        st.session_state.caixa_meses = opcoes_meses(st.session_state.filtro_ano)

    if "filtro_mes" not in st.session_state:
        st.session_state.filtro_mes = None

    if "caixa_filial" not in st.session_state:
        st.session_state.caixa_filial = opcoes_filiais(st.session_state.filtro_ano)

    if "filtro_filial" not in st.session_state:
        st.session_state.filtro_filial = None

    # GRAFICOS  ---------------------------------------------------------------------------------------

    # CAIXAS DE SELECAO - OPÇAO SELECIONADA
    if "filtro_grafico_margem" not in st.session_state:
        st.session_state.filtro_grafico_margem = 0

    if "filtro_grafico_receitas_e_custos" not in st.session_state:
        st.session_state.filtro_grafico_receitas_e_custos = 0
