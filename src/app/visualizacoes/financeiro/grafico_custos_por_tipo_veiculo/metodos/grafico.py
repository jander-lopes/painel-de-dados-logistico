import src.app.visualizacoes.uteis.graficos as graf
from src.app.controles.financeiro.custos_por_tipo_veiculo import ControleDadosSaida

from ....uteis.graficos import GraficoDadosEntrada
from .dados_customizados import dados_customizados
from .dica_ferramenta import dica_ferramenta


def grafico(dados_controle: ControleDadosSaida, dados_grafico: GraficoDadosEntrada):
    customizados = dados_customizados(dados_controle)
    dica = dica_ferramenta()
    cores = dados_grafico.cor
    return graf.colunas(dados_grafico, None, cores, customizados, dica, "h")
