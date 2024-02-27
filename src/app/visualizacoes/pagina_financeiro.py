import streamlit

from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .financeiro.grafico_custos_por_tipo_veiculo import grafico_custos_por_tipo_veiculo
from .financeiro.grafico_receitas_e_custos_por_filial import grafico_receitas_e_custos_por_filial
from .financeiro.graficos_margem import graficos_margem
from .financeiro.graficos_receitas_e_custos import graficos_receitas_e_custos
from .financeiro.inicializar import inicializar
from .financeiro.menu_lateral import menu_lateral
from .financeiro.metricas import cartoes_metricas
from .financeiro.tabela import tabela


def financeiro(st: streamlit) -> None:
    with open("./src/app/visualizacoes/financeiro/estilos/graficos.css") as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

    inicializar(st)

    requisicao = DadosRequisicao(
        st.session_state.filtro_ano,
        st.session_state.num_mes,
        st.session_state.filtro_filial,
        st.session_state.filtro_mes,
    )

    menu_lateral(st)

    cartoes_metricas(st, requisicao)

    st.markdown("___")
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        graficos_receitas_e_custos(st, requisicao)
    with col2:
        graficos_margem(st, requisicao)

    st.markdown("___")
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        grafico_receitas_e_custos_por_filial(st, requisicao)
    with col2:
        grafico_custos_por_tipo_veiculo(st, requisicao)

    st.markdown("___")
    st.write("")

    tabela(st, requisicao)

    # teste

    st.markdown("___")
    st.write("")
