import streamlit as streamlit

from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.visualizacoes.uteis.configurar_grafico import configurar_barra_ferramenta_grafico

from .custos_por_tipo_veiculo import desenhar


def grafico_custos_por_tipo_veiculo(st: streamlit, requisicao: DadosRequisicao) -> None:
    st.write(__titulo(requisicao))
    res = desenhar(requisicao)
    st.plotly_chart(res, use_container_width=True, **configurar_barra_ferramenta_grafico())


def __titulo(requisicao: DadosRequisicao) -> str:
    descritivo = "Custos por tipo de veículo -"
    if requisicao.mes and requisicao.filial:
        return f"{descritivo} {requisicao.filial} - {requisicao.mes}/{requisicao.ano}"

    if requisicao.mes:
        return f"{descritivo} {requisicao.mes}/{requisicao.ano}"

    if requisicao.filial:
        return f"{descritivo} {requisicao.filial} - {requisicao.ano}"

    return f"{descritivo} {requisicao.ano}"
