from dataclasses import dataclass

import pandas as pd

import src.app.infra.repositorio.financeiro.consultas as repo
from src.app.controles.uteis.diferenca_percentual import diferenca_percentual
from src.app.controles.uteis.indicador_acima_ou_abaixo_meta import indicador_acima_ou_abaixo_meta
from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from ..modelo_dados import ControleDadosSaida

Series = pd.Series


@dataclass
class ControleDadosEntrada:
    ano: Series
    num_mes: Series
    mes: Series
    receitas: Series
    custos: Series


def dados_entrada(requisicao: DadosRequisicao) -> ControleDadosEntrada:
    filtrar_colunas = ["ano", "num_mes", "mes", "receitas", "custos"]
    dados = repo.filtrar_por_ano_e_agrupar_por_ano_e_mes(requisicao.ano, filtrar_colunas)
    return ControleDadosEntrada(dados.ano, dados.num_mes, dados.mes, dados.receitas, dados.custos)


def dados_resposta(valor_monetario: Series, metas: Series, meses: Series) -> ControleDadosSaida:
    indicadores = pd.Series(indicador_acima_ou_abaixo_meta(valor_monetario, metas))
    taxa_cumprimento_meta = pd.Series(diferenca_percentual(valor_monetario, metas))
    return ControleDadosSaida(meses, valor_monetario, metas, indicadores, taxa_cumprimento_meta)
