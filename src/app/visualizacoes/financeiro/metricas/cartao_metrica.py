import streamlit as streamlit


def cartao(
    st: streamlit, titulo: str, valor: str | int | float, indicador: str | int | float, cor_indicador: str = "normal"
) -> None:
    st.metric(label=titulo, value=valor, delta=indicador, delta_color=cor_indicador)
