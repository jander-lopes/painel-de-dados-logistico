import src.app.visualizacoes.uteis.graficos as graf
from src.app.controles.financeiro.receitas_e_custos_por_filial import ControleDadosSaida
from src.app.uteis.formatar_unidades import formatar_valores_monetarios
from src.app.visualizacoes.uteis.cores_graf_barras import estilizar_cor_grafico_barras

from ....uteis.graficos import GraficoDadosEntrada
from .dados_customizados import dados_customizados
from .dica_ferramenta import dica_ferramenta


def grafico(dados_controle: ControleDadosSaida, dados_grafico: GraficoDadosEntrada):
    customizados = dados_customizados(dados_controle, dados_grafico.nome)
    dica = dica_ferramenta(dados_grafico.nome)[0]
    rotulo = formatar_valores_monetarios(dados_grafico.eixo_x)
    cores = estilizar_cor_grafico_barras(dados_grafico.cor, dados_grafico.cor_alerta, dados_controle.indicador)
    return graf.colunas(dados_grafico, rotulo, cores, customizados, dica, "h")
