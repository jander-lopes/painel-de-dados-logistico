import src.app.configuracao.cores as cor
import src.app.visualizacoes.uteis.graficos as graf

from ....uteis.graficos import GraficoDadosEntrada


def grafico(dados_grafico: GraficoDadosEntrada):
    cor_area = cor.area
    modelo = "%{text:.0f}%"
    dica = "<b style='font-size: 1rem'>%{text:.0f}%</b>"
    return graf.area(dados_grafico, cor_area, modelo, dica)
