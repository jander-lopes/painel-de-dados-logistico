from typing import Callable

import pandas as pd

from src.app.controles.financeiro.tabela_filial import controle
from src.app.infra.repositorio.modelo_dados import AtributosTabelaAnaliseFinanceira, DadosRequisicao, Medidas
from src.app.uteis.formatar_unidades import formatar_valores_monetarios, formatar_valores_percentil

DataFrame = pd.DataFrame


_financeiro = AtributosTabelaAnaliseFinanceira()
_medida = Medidas()


def desenhar(requisicao: DadosRequisicao) -> DataFrame:
    dados_entrada = controle(requisicao)
    resposta = __dados_resposta(dados_entrada)
    return resposta


def __dados_resposta(dados: DataFrame) -> DataFrame:
    res = pd.DataFrame()
    res[_financeiro.filial] = dados[_financeiro.filial].copy()
    res[_financeiro.receitas] = formatar_valores_monetarios(dados[_financeiro.receitas], 0, "R$")
    res[_financeiro.custos] = formatar_valores_monetarios(dados[_financeiro.custos], 0, "R$")
    res[_financeiro.qnt_pedidos] = dados[_financeiro.qnt_pedidos].astype("str")
    res[_medida.resultado] = formatar_valores_monetarios(dados[_medida.resultado], 0, "R$")
    res[_medida.ticket_medio] = formatar_valores_monetarios(dados[_medida.ticket_medio], 0, "R$")
    res[_medida.margem] = formatar_valores_percentil(dados[_medida.margem], 1)

    estilizar_atributos = [_medida.resultado, _medida.ticket_medio, _medida.margem]
    return __estilizar_resposta(res, __mudar_cor_valores_negativos, estilizar_atributos)


def __estilizar_resposta(dados: DataFrame, funcao_retorno: Callable, atributos: list[str]):
    return dados.style.apply(
        funcao_retorno,
        subset=atributos,
    )


def __mudar_cor_valores_negativos(atributos: list[str]) -> list[str]:
    return ["background-color: rgba(255,0,0,0.05);" if "-" in atributo else None for atributo in atributos]
