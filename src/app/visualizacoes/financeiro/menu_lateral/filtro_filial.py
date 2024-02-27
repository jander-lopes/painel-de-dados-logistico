import streamlit as streamlit


def filtro_filial(st: streamlit):
    def limpar_filtro_filial():
        st.session_state.filtro_filial = None

    col1, col2 = st.columns([5, 1])
    with col1:
        opcao = st.selectbox(
            label="Filial:",
            options=st.session_state.caixa_filial,
            index=(
                st.session_state.caixa_filial.index(st.session_state.filtro_filial)
                if st.session_state.filtro_filial
                else None
            ),
            placeholder="Selecione a filial",
            key="filtro_filial",
        )

    desabilitar_botao = False if opcao else True

    with col2:
        st.button(label="\u2718", key="btn_filial", on_click=limpar_filtro_filial, disabled=desabilitar_botao)
