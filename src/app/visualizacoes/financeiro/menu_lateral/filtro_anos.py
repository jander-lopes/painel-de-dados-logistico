import streamlit as streamlit

from src.app.visualizacoes.uteis.opcoes_caixas_texto import opcoes_meses


def filtro_anos(st: streamlit):
    def alteracao_caixa_selecao_ano():
        st.session_state.caixa_meses = opcoes_meses(st.session_state.filtro_ano)
        if st.session_state.filtro_mes not in st.session_state.caixa_meses or st.session_state.filtro_mes == None:
            st.session_state.filtro_mes = None
            st.session_state.num_mes = None

    col1, col2 = st.columns([5, 1])
    with col1:
        st.selectbox(
            label="Ano:",
            options=st.session_state.caixa_ano,
            index=len(st.session_state.caixa_ano) - 1,
            placeholder="Selecione o ano",
            key="filtro_ano",
            on_change=alteracao_caixa_selecao_ano,
        )
