from pandas import Series

import src.congifuracao.variaveis as var
from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .modelo_dados import ControleDadosSaida
from .uteis.metodos_receitas_ou_custos_meses import dados_entrada, dados_resposta


def controle(requisicao: DadosRequisicao) -> ControleDadosSaida:
    dados = dados_entrada(requisicao)
    metas = __calcular_metas(dados.receitas)
    resposta = dados_resposta(dados.custos, metas, dados.mes)
    return resposta


def __calcular_metas(receitas: Series) -> Series:
    return receitas * var.CUSTOS_SOBRE_RECEITA
