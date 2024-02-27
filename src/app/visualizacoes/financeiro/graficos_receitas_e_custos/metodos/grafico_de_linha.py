import src.app.visualizacoes.uteis.graficos as graf
from src.app.controles.financeiro.modelo_dados import ControleDadosSaida
from src.app.uteis.formatar_unidades import formatar_valores_monetarios

from ....uteis.graficos import GraficoDadosEntrada
from .dica_graficos import dica_graf_linha


def graf_linha(dados_controle: ControleDadosSaida, dados_grafico: GraficoDadosEntrada):
    customizados = formatar_valores_monetarios(dados_controle.metas, 1)
    dica = dica_graf_linha(dados_grafico.nome.value)
    cores = dados_grafico.cor
    return graf.linha(dados_grafico, cores, customizados, dica)
