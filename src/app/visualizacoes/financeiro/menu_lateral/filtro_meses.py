import streamlit as streamlit


def filtro_meses(st: streamlit):
    def limpar_filtro_mes():
        st.session_state.filtro_mes = None
        st.session_state.num_mes = None

    def alteracao_caixa_selecao_mes():
        st.session_state.num_mes = (
            st.session_state.caixa_meses.index(st.session_state.filtro_mes) + 1 if st.session_state.filtro_mes else None
        )

    col1, col2 = st.columns([5, 1])
    with col1:
        opcao = st.selectbox(
            label="Mês:",
            options=st.session_state.caixa_meses,
            index=(
                st.session_state.caixa_meses.index(st.session_state.filtro_mes) if st.session_state.filtro_mes else None
            ),
            placeholder="Selecione o mês",
            key="filtro_mes",
            on_change=alteracao_caixa_selecao_mes,
        )

    desabilitar_botao = False if opcao else True

    with col2:
        st.button(label="\u2718", key="btn_mes", on_click=limpar_filtro_mes, disabled=desabilitar_botao)
