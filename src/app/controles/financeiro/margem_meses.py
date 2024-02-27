from dataclasses import dataclass

from pandas import DataFrame, Series

import src.app.infra.repositorio.financeiro.consultas as repo
from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .modelo_dados import ControleDadosSaida
from .uteis.medidas import margem, resultado


@dataclass
class ControleDadosEntrada:
    ano: Series
    num_mes: Series
    mes: Series
    receitas: Series
    custos: Series


def controle(requisicao: DadosRequisicao) -> DataFrame:
    dados_entrada = __dados_entrada(requisicao)
    resposta = __dados_resposta(dados_entrada)
    return resposta


def __dados_entrada(requisicao: DadosRequisicao) -> ControleDadosEntrada:
    filtrar_colunas = ["ano", "num_mes", "mes", "receitas", "custos"]
    dados = repo.filtrar_por_ano_e_agrupar_por_ano_e_mes(requisicao.ano, filtrar_colunas)
    return ControleDadosEntrada(dados.ano, dados.num_mes, dados.mes, dados.receitas, dados.custos)


def __dados_resposta(dados: ControleDadosEntrada) -> ControleDadosSaida:
    medida_margem = __calcular_margem(dados)
    return ControleDadosSaida(dados.mes, medida_margem)


def __calcular_margem(dados: ControleDadosEntrada) -> Series:
    medida_resultado = resultado(dados.receitas, dados.custos)
    medida_margem = margem(medida_resultado, dados.receitas)
    return medida_margem
