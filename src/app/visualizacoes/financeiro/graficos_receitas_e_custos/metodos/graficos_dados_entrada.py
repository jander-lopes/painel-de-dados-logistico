import src.app.configuracao.cores as cor
from src.app.controles.financeiro.modelo_dados import ControleDadosSaida

from ....uteis.graficos import GraficoDadosEntrada
from ...uteis.nomes_dos_graficos import NomeGraficos


def dados_barra(dados: ControleDadosSaida, nome_grafico: NomeGraficos, cor: str, cor_alerta: str):
    return GraficoDadosEntrada(dados.eixo_x, dados.eixo_y, nome_grafico, cor, cor_alerta)


def dados_linha(dados: ControleDadosSaida, nome_grafico: NomeGraficos, cor: str, xaxis: str | None = None):
    return GraficoDadosEntrada(dados.eixo_x, dados.metas, nome_grafico, cor, None, xaxis)
