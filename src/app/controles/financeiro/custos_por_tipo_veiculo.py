from dataclasses import dataclass

from pandas import DataFrame, Series

import src.app.infra.repositorio.financeiro.consultas as repo
from src.app.infra.repositorio.modelo_dados import DadosRequisicao


@dataclass
class ControleDadosEntrada:
    tipo_veiculo: Series
    abastecimento: Series
    manutencao: Series
    custo_fixo: Series
    custos: Series


@dataclass
class ControleDadosSaida:
    tipo_veiculo: Series
    abastecimento: Series
    manutencao: Series
    fixos: Series
    custos: Series
    repre_abastecimento: Series
    repre_manutencao: Series
    repre_fixos: Series
    repre_custo: Series


def controle(requisicao: DadosRequisicao) -> ControleDadosSaida:
    dados_entrada = __dados_entrada(requisicao)
    resposta = __dados_resposta(dados_entrada)
    return resposta


def __dados_entrada(requisicao: DadosRequisicao) -> ControleDadosEntrada:
    dados = __filtrar_dados_entrada(requisicao)
    return ControleDadosEntrada(
        dados.tipo_veiculo,
        dados.abastecimento,
        dados.manutencao,
        dados.custo_fixo,
        dados.custos,
    )


def __filtrar_dados_entrada(requisicao: DadosRequisicao) -> DataFrame:
    if requisicao.num_mes and requisicao.filial:
        return repo.filtrar_por_ano_mes_e_filial_e_agrupar_por_ano_mes_e_filial_e_tipo_veiculo(
            requisicao.ano, requisicao.num_mes, requisicao.filial
        )
    if requisicao.num_mes:
        return repo.filtrar_por_ano_e_mes_e_agrupar_por_ano_mes_e_tipo_veiculo(requisicao.ano, requisicao.num_mes)
    if requisicao.filial:
        return repo.filtrar_por_ano_e_filial_e_agrupar_por_ano_filial_e_tipo_veiculo(requisicao.ano, requisicao.filial)
    return repo.filtrar_por_ano_e_agrupar_por_ano_e_tipo_veiculo(requisicao.ano)


def __dados_resposta(dados: ControleDadosEntrada) -> ControleDadosSaida:
    custos_totais = dados.custos.sum()
    return ControleDadosSaida(
        dados.tipo_veiculo,
        dados.abastecimento,
        dados.manutencao,
        dados.custo_fixo,
        dados.custos,
        __representa_do_total(dados.abastecimento, dados.custos),
        __representa_do_total(dados.manutencao, dados.custos),
        __representa_do_total(dados.custo_fixo, dados.custos),
        __representa_do_total(dados.custos, custos_totais),
    )


def __representa_do_total(valor: Series, total: int | float) -> Series:
    return (valor / total) * 100
