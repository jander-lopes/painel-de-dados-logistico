import src.app.configuracao.cores as cor
from src.app.controles.financeiro.modelo_dados import ControleDadosSaida

from ....uteis.graficos import GraficoDadosEntrada
from ...uteis.nomes_dos_graficos import NomeGraficos


def dados_graf(dados: ControleDadosSaida):
    return GraficoDadosEntrada(dados.eixo_x, dados.eixo_y, NomeGraficos.MARGEM, cor.margem)
