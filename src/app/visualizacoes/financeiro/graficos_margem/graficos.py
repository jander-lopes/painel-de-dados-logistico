import streamlit as streamlit

from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.visualizacoes.uteis.configurar_grafico import configurar_barra_ferramenta_grafico

from .margem_anual import desenhar as desenhar_margem_anual
from .margem_meses import desenhar as desenhar_margem_meses


def graficos_margem(st: streamlit, requisicao: DadosRequisicao) -> None:

    opcoes = ["Margem - Anual", f"Margem - {requisicao.ano}"]

    def __alteracao_caixa_selecao():
        st.session_state.filtro_grafico_margem = opcoes.index(st.session_state.margem)

    selecao = st.selectbox(
        label="Selecione o gráfico:",
        options=opcoes,
        index=st.session_state.filtro_grafico_margem,
        key="margem",
        on_change=__alteracao_caixa_selecao,
    )

    match selecao:
        case selecao if selecao == opcoes[0]:
            res = desenhar_margem_anual()
            st.plotly_chart(res, use_container_width=True, **configurar_barra_ferramenta_grafico())
        case selecao if selecao == opcoes[1]:
            res = desenhar_margem_meses(requisicao)
            st.plotly_chart(res, use_container_width=True, **configurar_barra_ferramenta_grafico())
