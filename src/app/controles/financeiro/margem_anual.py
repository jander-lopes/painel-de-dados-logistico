from dataclasses import dataclass

from pandas import Series

import src.app.infra.repositorio.financeiro.consultas as repo

from .modelo_dados import ControleDadosSaida
from .uteis.medidas import margem, resultado


@dataclass
class ControleDadosEntrada:
    ano: Series
    receitas: Series
    custos: Series


def controle() -> ControleDadosSaida:
    dados_entrada = __dados_entrada()
    resposta = __dados_resposta(dados_entrada)
    return resposta


def __dados_entrada() -> ControleDadosEntrada:
    dados = repo.agrupar_por_ano()
    return ControleDadosEntrada(ano=dados.ano, receitas=dados.receitas, custos=dados.custos)


def __dados_resposta(dados: ControleDadosEntrada) -> ControleDadosSaida:
    medida_margem = __calcular_margem(dados)
    return ControleDadosSaida(dados.ano, medida_margem)


def __calcular_margem(dados: ControleDadosEntrada) -> Series:
    medida_resultado = resultado(dados.receitas, dados.custos)
    medida_margem = margem(medida_resultado, dados.receitas)
    return medida_margem
