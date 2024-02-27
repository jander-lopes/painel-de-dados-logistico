from dataclasses import dataclass

import pandas as pd

import src.app.infra.repositorio.financeiro.consultas as repo
import src.congifuracao.variaveis as var
from src.app.controles.uteis.diferenca_percentual import diferenca_percentual
from src.app.controles.uteis.indicador_acima_ou_abaixo_meta import indicador_acima_ou_abaixo_meta

from .modelo_dados import ControleDadosSaida

Series = pd.Series


@dataclass
class ControleDadosEntrada:
    ano: Series
    receitas: Series
    custos: Series
    metas_receitas: Series


def controle() -> ControleDadosSaida:
    dados_entrada = __dados_entrada()
    resposta = __dados_resposta(dados_entrada)
    return resposta


def __dados_entrada() -> ControleDadosEntrada:
    dados = repo.agrupar_receitas_custos_e_metas_por_ano()
    return ControleDadosEntrada(dados.ano, dados.receitas, dados.custos, dados.metas_receitas)


def __dados_resposta(dados: ControleDadosEntrada) -> list[ControleDadosSaida]:
    indicador_receitas, taxa_receitas = __medidas_receitas(dados)
    metas_custos, indicador_custos, taxa_custos = __medidas_custos(dados)
    return [
        ControleDadosSaida(dados.ano, dados.receitas, dados.metas_receitas, indicador_receitas, taxa_receitas),
        ControleDadosSaida(dados.ano, dados.custos, metas_custos, indicador_custos, taxa_custos),
    ]


def __medidas_receitas(dados: ControleDadosEntrada) -> tuple[Series]:
    indicador = pd.Series(indicador_acima_ou_abaixo_meta(dados.receitas, dados.metas_receitas))
    taxa_cump_meta = pd.Series(diferenca_percentual(dados.receitas, dados.metas_receitas))
    return indicador, taxa_cump_meta


def __medidas_custos(dados: ControleDadosEntrada) -> tuple[Series]:
    metas_custos = __calcular_meta_custos(dados.receitas)
    indicador = pd.Series(indicador_acima_ou_abaixo_meta(dados.custos, metas_custos))
    taxa_cump_meta = pd.Series(diferenca_percentual(dados.custos, metas_custos))
    return metas_custos, indicador, taxa_cump_meta


def __calcular_meta_custos(receitas: Series) -> Series:
    return receitas * var.CUSTOS_SOBRE_RECEITA
