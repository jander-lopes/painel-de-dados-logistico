from dataclasses import dataclass

import pandas as pd

import src.app.infra.bd.tabelas as tb

from ..modelo_dados import AtributosTabelaAnaliseFinanceira, AtributosTabelaMetas, DadosRequisicao

DataFrame = pd.DataFrame


_attr = AtributosTabelaAnaliseFinanceira()
_meta = AtributosTabelaMetas()


@dataclass
class DadosFiltro:
    atributos: list[str]
    consulta: str
    agrupar_por: list[str]


# OK
def filtrar_por_ano_e_agrupar_por_ano_e_filiais(requisicao: DadosRequisicao) -> DataFrame:
    dados_filtro = DadosFiltro(
        [_attr.ano, _attr.filial, _attr.qnt_pedidos, _attr.receitas, _attr.custos],
        f"ano == {requisicao.ano}",
        [_attr.ano, _attr.filial],
    )
    return __filtrar_dados(dados_filtro).copy()


# OK
def filtrar_por_ano_e_mes_e_agrupar_por_ano_mes_e_filiais(requisicao: DadosRequisicao) -> DataFrame:
    dados_filtro = DadosFiltro(
        [
            _attr.ano,
            _attr.num_mes,
            _attr.filial,
            _attr.qnt_pedidos,
            _attr.receitas,
            _attr.custos,
        ],
        f"ano == {requisicao.ano} & num_mes == {requisicao.num_mes}",
        [_attr.ano, _attr.num_mes, _attr.filial],
    )
    return __filtrar_dados(dados_filtro).copy()


# OK
def filtrar_ano_atual_e_ano_anterior_e_agrupar_por_ano(requisicao: DadosRequisicao) -> DataFrame:
    dados_filtro = DadosFiltro(
        [_attr.ano, _attr.receitas, _attr.custos],
        f"{requisicao.ano - 1} <= ano <= {requisicao.ano}",
        [_attr.ano],
    )
    return __filtrar_dados(dados_filtro).copy()


# OK VERIFICAR SAIDA SEM A NECESSIDADE DE AGRUPAR
def filtrar_ano_e_mes_atual_e_ano_mes_anterior_e_agrupar_por_ano_e_mes(requisicao: DadosRequisicao) -> DataFrame:
    dados_filtro = DadosFiltro(
        [_attr.ano, _attr.num_mes, _attr.receitas, _attr.custos],
        f"{requisicao.ano - 1} <= ano <= {requisicao.ano} & num_mes == {requisicao.num_mes}",
        [_attr.ano, _attr.num_mes],
    )
    return __filtrar_dados(dados_filtro).copy()


# OK
def agrupar_por_ano():
    filtro_atributos = [_attr.ano, _attr.receitas, _attr.custos]
    dados = tb.dados_analise_financeira()[filtro_atributos].groupby(_attr.ano).sum().reset_index()
    return dados.copy()


# OK
def agrupar_receitas_custos_e_metas_por_ano() -> DataFrame:
    dados = agrupar_por_ano()
    dados_metas = tb.tb_metas()
    juntar_dados = pd.merge(dados, dados_metas, how="left", on=_attr.ano)
    return juntar_dados.copy()


# OK
def filtrar_por_ano_e_agrupar_por_ano_e_mes(ano: int, colunas: list[str]) -> DataFrame:
    dados_filtro = DadosFiltro(
        [_attr.ano, _attr.num_mes, _attr.mes, _attr.receitas, _attr.custos],
        f"ano == {ano}",
        [_attr.ano, _attr.num_mes, _attr.mes],
    )
    return __filtrar_dados(dados_filtro)[colunas].copy()


# OK
def filtrar_por_ano_e_agrupar_por_ano_e_tipo_veiculo(ano: int) -> DataFrame:
    col_base = __colunas_filtro_dados_por_tipo_veiculo()
    dados_filtro = DadosFiltro(
        col_base,
        f"ano == {ano}",
        [_attr.ano, _attr.tipo_veiculo],
    )
    return __filtrar_dados(dados_filtro)[col_base[1:]].copy()


# OK
def filtrar_por_ano_e_filial_e_agrupar_por_ano_filial_e_tipo_veiculo(ano: int, filial: str) -> DataFrame:
    col_base = __colunas_filtro_dados_por_tipo_veiculo()
    dados_filtro = DadosFiltro(
        [_attr.filial, *col_base],
        f"ano == {ano} & filial == '{filial}'",
        [_attr.ano, _attr.filial, _attr.tipo_veiculo],
    )
    return __filtrar_dados(dados_filtro)[col_base[1:]].copy()


# OK
def filtrar_por_ano_e_mes_e_agrupar_por_ano_mes_e_tipo_veiculo(ano: int, num_mes: int) -> DataFrame:
    col_base = __colunas_filtro_dados_por_tipo_veiculo()
    dados_filtro = DadosFiltro(
        [_attr.num_mes, *col_base],
        f"ano == {ano} & num_mes == {num_mes}",
        [_attr.ano, _attr.num_mes, _attr.tipo_veiculo],
    )
    return __filtrar_dados(dados_filtro)[col_base[1:]].copy()


# OK
def filtrar_por_ano_mes_e_filial_e_agrupar_por_ano_mes_e_filial_e_tipo_veiculo(
    ano: int, num_mes: int, filial: str
) -> DataFrame:
    col_base = __colunas_filtro_dados_por_tipo_veiculo()
    dados_filtro = DadosFiltro(
        [_attr.num_mes, _attr.filial, *col_base],
        f"ano == {ano} & num_mes == {num_mes} & filial == '{filial}'",
        [_attr.ano, _attr.num_mes, _attr.filial, _attr.tipo_veiculo],
    )
    return __filtrar_dados(dados_filtro)[col_base[1:]].copy()


def __colunas_filtro_dados_por_tipo_veiculo() -> list[str]:
    return [
        _attr.ano,
        _attr.tipo_veiculo,
        _attr.abastecimento,
        _attr.manutencao,
        _attr.custo_fixo,
        _attr.custos,
    ]


def __filtrar_dados(dados_entrada: DadosFiltro) -> DataFrame:
    return (
        tb.dados_analise_financeira()[dados_entrada.atributos]
        .query(dados_entrada.consulta)
        .groupby(dados_entrada.agrupar_por)
        .sum()
        .reset_index()
    )


def meta_ano_atual(ano: int) -> float:
    meta = tb.tb_metas().query(f"ano == {ano}")[_meta.receitas].values[0]
    return float(meta)


def lista_anos() -> list[int]:
    return tb.dados_analise_financeira()[_attr.ano].unique().tolist()


def lista_meses(ano: int) -> list[int]:
    return tb.dados_analise_financeira()[[_attr.ano, _attr.mes]].query(f"ano == {ano}")[_attr.mes].unique().tolist()


def lista_filiais(ano: int) -> list[int]:
    return tb.dados_analise_financeira().query(f"ano == {ano}")[_attr.filial].unique().tolist()
