import streamlit as st

st.set_page_config(layout="wide", page_title="Painel Financeiro", initial_sidebar_state="collapsed")

from src.app.compor_visualizacoes import iniciar_aplicativo

iniciar_aplicativo(st)
