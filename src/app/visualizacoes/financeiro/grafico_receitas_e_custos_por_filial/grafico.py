import streamlit as streamlit

from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.visualizacoes.uteis.configurar_grafico import configurar_barra_ferramenta_grafico

from .receitas_custos_por_filial import desenhar


def grafico_receitas_e_custos_por_filial(st: streamlit, requisicao: DadosRequisicao) -> None:
    st.write(__titulo(requisicao))
    res = desenhar(requisicao)
    st.plotly_chart(res, use_container_width=True, **configurar_barra_ferramenta_grafico())


def __titulo(requiscao: DadosRequisicao) -> str:
    if requiscao.mes:
        return f"Receitas e Custos por filial - {requiscao.mes}/{requiscao.ano}"
    return f"Receitas e Custos por filial - {requiscao.ano}"
