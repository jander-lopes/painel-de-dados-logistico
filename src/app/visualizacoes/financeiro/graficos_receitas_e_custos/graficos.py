import streamlit as streamlit

from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.visualizacoes.uteis.configurar_grafico import configurar_barra_ferramenta_grafico

from .custos_meses import desenhar as desenhar_custos
from .receitas_e_custos_anual import desenhar as desenhar_receitas_e_custos
from .receitas_meses import desenhar as desenhar_receitas


def graficos_receitas_e_custos(st: streamlit, requisicao: DadosRequisicao) -> None:

    opcoes = ["Receitas x Custos - Anual", f"Receitas - {requisicao.ano}", f"Custos - {requisicao.ano}"]

    def __alteracao_caixa_selecao():
        st.session_state.filtro_grafico_receitas_e_custos = opcoes.index(st.session_state.receitas_e_custos)

    selecao = st.selectbox(
        label="Selecione o gráfico:",
        options=opcoes,
        index=st.session_state.filtro_grafico_receitas_e_custos,
        key="receitas_e_custos",
        on_change=__alteracao_caixa_selecao,
    )

    match selecao:
        case selecao if selecao == opcoes[0]:
            res = desenhar_receitas_e_custos()
            st.plotly_chart(res, use_container_width=True, **configurar_barra_ferramenta_grafico())
        case selecao if selecao == opcoes[1]:
            res = desenhar_receitas(requisicao)
            st.plotly_chart(res, use_container_width=True, **configurar_barra_ferramenta_grafico())
        case selecao if selecao == opcoes[2]:
            res = desenhar_custos(requisicao)
            st.plotly_chart(res, use_container_width=True, **configurar_barra_ferramenta_grafico())
