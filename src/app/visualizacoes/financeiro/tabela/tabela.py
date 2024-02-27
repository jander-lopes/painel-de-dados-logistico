import streamlit as streamlit

from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .tratar_dados import desenhar


def tabela(st: streamlit, requisicao: DadosRequisicao) -> None:
    dados = desenhar(requisicao)

    st.write(__titulo(requisicao))

    st.dataframe(
        dados,
        column_config=dict(
            filial="Filial",
            qnt_pedidos="Quant. Pedidos",
            receitas="Receitas",
            custos="Custos",
            resultado="Resultado",
            ticket_medio="Ticket Médio",
            margem="Margem",
        ),
        hide_index=True,
        use_container_width=True,
    )


def __titulo(requisicao: DadosRequisicao) -> str:
    titulo = f"Receitas e Custos por Filial - {requisicao.ano}"
    if requisicao.mes:
        titulo = f"Receitas e Custos por Filial - {requisicao.mes} de {requisicao.ano}"
    return titulo
