import streamlit as streamlit

from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .cartao_metrica import cartao
from .metricas import resposta


def cartoes_metricas(st: streamlit, requisicao: DadosRequisicao) -> None:

    dados = resposta(requisicao)

    col1, col2 = st.columns(2)
    with col1:
        col10, col11 = st.columns(2)
        with col10:
            titulo = __titulo(requisicao, "Receitas")
            indicador = __indicador(dados.indicador.receita)
            cartao(st, titulo, dados.receita, indicador)
        with col11:
            titulo = __titulo(requisicao, "Custos")
            indicador = __indicador(dados.indicador.custo)
            cartao(st, titulo, dados.custo, indicador, "inverse")

    with col2:
        col20, col21 = st.columns(2)
        with col20:
            titulo = __titulo(requisicao, "Resultado")
            indicador = __indicador(dados.indicador.resultado)
            cartao(st, titulo, dados.resultado, indicador)

        with col21:
            titulo = __titulo(requisicao, "Margem")
            indicador = __indicador(dados.indicador.margem)
            cartao(st, titulo, dados.margem, indicador)


def __titulo(requisicao: DadosRequisicao, descricao: str) -> str:
    titulo = f"{descricao} - {requisicao.ano}"
    if requisicao.mes:
        titulo = f"{descricao} - {requisicao.mes}/{requisicao.ano}"
    return titulo


def __indicador(indicador: str) -> str:
    if not indicador:
        return None
    if "-" in indicador:
        return f"{indicador} \n abaixo ano anterior"
    return f"{indicador} \n acima ano anterior"
