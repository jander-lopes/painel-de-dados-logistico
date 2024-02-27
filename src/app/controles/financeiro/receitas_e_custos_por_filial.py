from dataclasses import dataclass

import pandas as pd

import src.app.infra.repositorio.financeiro.consultas as repo
import src.congifuracao.variaveis as var
from src.app.controles.uteis.diferenca_percentual import diferenca_percentual
from src.app.controles.uteis.indicador_acima_ou_abaixo_meta import indicador_acima_ou_abaixo_meta
from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .uteis.medidas import resultado

Series = pd.Series
DataFrame = pd.DataFrame


@dataclass
class ControleDadosEntrada:
    filial: Series
    receitas: Series
    custos: Series


@dataclass
class ControleDadosSaida:
    filial: Series
    receitas: Series
    custos: Series
    resultados: Series
    indicador: Series
    taxa_limite_custos: Series


def controle(requisicao: DadosRequisicao) -> ControleDadosSaida:
    dados_entrada = __dados_entrada(requisicao)
    resposta = __dados_resposta(dados_entrada)
    return resposta


def __dados_entrada(requisicao: DadosRequisicao) -> ControleDadosEntrada:
    dados = __filtrar_dados_entrada(requisicao)
    return ControleDadosEntrada(dados.filial, dados.receitas, dados.custos)


def __filtrar_dados_entrada(requisicao: DadosRequisicao) -> DataFrame:
    if requisicao.num_mes:
        return repo.filtrar_por_ano_e_mes_e_agrupar_por_ano_mes_e_filiais(requisicao)
    return repo.filtrar_por_ano_e_agrupar_por_ano_e_filiais(requisicao)


def __dados_resposta(dados: ControleDadosEntrada) -> list[ControleDadosSaida]:
    medida_resultado = resultado(dados.receitas, dados.custos)
    limite_custos = __calcular_limite_de_custos(dados.receitas)
    indicador = pd.Series(indicador_acima_ou_abaixo_meta(dados.custos, limite_custos))
    taxa_limite_custo = diferenca_percentual(dados.custos, limite_custos)
    return ControleDadosSaida(
        dados.filial, dados.receitas, dados.custos, medida_resultado, indicador, taxa_limite_custo
    )


def __calcular_limite_de_custos(receitas: ControleDadosEntrada) -> Series:
    return receitas * var.CUSTOS_SOBRE_RECEITA
