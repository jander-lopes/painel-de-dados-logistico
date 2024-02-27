import src.app.configuracao.cores as cor
from src.app.controles.financeiro.receitas_e_custos_por_filial import ControleDadosSaida

from ....uteis.graficos import GraficoDadosEntrada
from ...uteis.nomes_dos_graficos import NomeGraficos


def dados_receitas(entrada: ControleDadosSaida) -> GraficoDadosEntrada:
    return GraficoDadosEntrada(entrada.receitas, entrada.filial, NomeGraficos.RECEITA, cor.receitas)


def dados_custos(entrada: ControleDadosSaida) -> GraficoDadosEntrada:
    return GraficoDadosEntrada(entrada.custos, entrada.filial, NomeGraficos.CUSTO, cor.limite_de_custo, cor.custos)
