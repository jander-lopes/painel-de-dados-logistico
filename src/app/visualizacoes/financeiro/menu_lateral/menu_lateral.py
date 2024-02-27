import streamlit as streamlit

from .filtro_anos import filtro_anos
from .filtro_filial import filtro_filial
from .filtro_meses import filtro_meses


def menu_lateral(st: streamlit):

    with st.sidebar:
        st.title("Filtros")

        filtro_anos(st)

        filtro_meses(st)

        filtro_filial(st)
