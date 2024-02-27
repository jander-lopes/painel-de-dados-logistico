import pandas as pd

import src.app.infra.repositorio.financeiro.consultas as repo
from src.app.controles.uteis.compor_meta_ano_diluida_por_meses import meta_ano_diluida_por_meses
from src.app.infra.repositorio.modelo_dados import DadosRequisicao

from .modelo_dados import ControleDadosSaida
from .uteis.metodos_receitas_ou_custos_meses import dados_entrada, dados_resposta

Series = pd.Series


def controle(requisicao: DadosRequisicao) -> ControleDadosSaida:
    dados = dados_entrada(requisicao)
    metas = __calcular_metas(requisicao.ano, dados.num_mes.to_list())
    resposta = dados_resposta(dados.receitas, metas, dados.mes)
    return resposta


def __calcular_metas(ano_atual: int, meses: list[int]) -> Series:
    meta_ano_atual = repo.meta_ano_atual(ano_atual)
    metas = meta_ano_diluida_por_meses(ano_atual, meta_ano_atual)
    return pd.Series(metas)[: len(meses)]
