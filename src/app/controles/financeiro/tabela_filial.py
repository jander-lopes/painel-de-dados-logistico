import pandas as pd

import src.app.infra.repositorio.financeiro.consultas as repo
from src.app.infra.repositorio.modelo_dados import AtributosTabelaAnaliseFinanceira, DadosRequisicao, Medidas

from .uteis.medidas import margem, resultado, ticket_medio

DataFrame = pd.DataFrame

_financeiro = AtributosTabelaAnaliseFinanceira()
_medida = Medidas()


def controle(requisicao: DadosRequisicao) -> DataFrame:
    dados = __coletar_dados(requisicao)
    __calcular_medidas(dados)
    return __resposta(dados)


def __coletar_dados(requisicao: DadosRequisicao) -> DataFrame:
    if requisicao.num_mes:
        return repo.filtrar_por_ano_e_mes_e_agrupar_por_ano_mes_e_filiais(requisicao)
    return repo.filtrar_por_ano_e_agrupar_por_ano_e_filiais(requisicao)


def __calcular_medidas(dados: DataFrame) -> DataFrame:
    dados[_medida.resultado] = resultado(dados[_financeiro.receitas], dados[_financeiro.custos])
    dados[_medida.ticket_medio] = ticket_medio(dados[_financeiro.receitas], dados[_financeiro.qnt_pedidos])
    dados[_medida.margem] = margem(dados[_medida.resultado], dados[_financeiro.receitas])


def __resposta(dados: DataFrame) -> DataFrame:
    excluir_colunas = [_financeiro.ano, _financeiro.num_mes]
    return dados[dados.columns.difference(excluir_colunas)]
