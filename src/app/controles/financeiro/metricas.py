from dataclasses import dataclass

import numpy as np
from pandas import DataFrame

import src.app.infra.repositorio.financeiro.consultas as repo
from src.app.controles.uteis.diferenca_percentual import diferenca_percentual
from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .uteis.medidas import margem, resultado

Numero = np.float64 | np.int64


@dataclass
class DadosAno:
    receita: int | float | None = None
    custo: int | float | None = None


@dataclass
class ControleDadosEntrada:
    ano_anterior: DadosAno
    ano_atual: DadosAno


@dataclass
class DadosMedidas:
    resultado: int | float
    margem: int | float
    resultado_anterior: int | float
    margem_anterior: int | float


@dataclass
class DadosIndicadores:
    receita: int | float | None = None
    custo: int | float | None = None
    resultado: int | float | None = None
    margem: int | float | None = None


@dataclass
class ControleDadosSaida:
    receita: Numero
    custo: Numero
    resultado: Numero
    margem: Numero
    indicador: DadosIndicadores


def controle(requisicao: DadosRequisicao) -> ControleDadosSaida:
    dados_entrada = __dados_entrada(requisicao)
    resposta = __dados_resposta(dados_entrada)
    return resposta


def __dados_entrada(requisicao: DadosRequisicao) -> ControleDadosEntrada:
    dados = __filtrar_dados_entrada(requisicao)
    if len(dados) > 1:
        return ControleDadosEntrada(
            DadosAno(dados.iloc[0].receitas, dados.iloc[0].custos),
            DadosAno(dados.iloc[1].receitas, dados.iloc[1].custos),
        )
    return ControleDadosEntrada(DadosAno(), DadosAno(dados.iloc[0].receitas, dados.iloc[0].custos))


def __filtrar_dados_entrada(requisicao: DadosRequisicao) -> DataFrame:
    if requisicao.num_mes:
        return repo.filtrar_ano_e_mes_atual_e_ano_mes_anterior_e_agrupar_por_ano_e_mes(requisicao)
    return repo.filtrar_ano_atual_e_ano_anterior_e_agrupar_por_ano(requisicao)


def __dados_resposta(dados: ControleDadosEntrada) -> ControleDadosSaida:
    ano_atual = __calcular_medidas(dados.ano_atual)
    ano_anterior = __calcular_medidas(dados.ano_anterior) if dados.ano_anterior.receita else [0, 0]
    medidas = DadosMedidas(*ano_atual, *ano_anterior)
    indicadores = (
        __calcular_diferenca_percentual_entre_anos(dados, medidas) if dados.ano_anterior.receita else DadosIndicadores()
    )
    return ControleDadosSaida(
        dados.ano_atual.receita, dados.ano_atual.custo, medidas.resultado, medidas.margem, indicadores
    )


def __calcular_medidas(dados: DadosAno) -> list[Numero]:
    medida_resultado = resultado(dados.receita, dados.custo)
    medida_margem = margem(medida_resultado, dados.receita)
    return medida_resultado, medida_margem


def __calcular_diferenca_percentual_entre_anos(dados: ControleDadosEntrada, medidas: DadosMedidas) -> DadosIndicadores:
    return DadosIndicadores(
        diferenca_percentual(dados.ano_atual.receita, dados.ano_anterior.receita),
        diferenca_percentual(dados.ano_atual.custo, dados.ano_anterior.custo),
        diferenca_percentual(medidas.resultado, medidas.resultado_anterior),
        diferenca_percentual(medidas.margem, medidas.margem_anterior),
    )
