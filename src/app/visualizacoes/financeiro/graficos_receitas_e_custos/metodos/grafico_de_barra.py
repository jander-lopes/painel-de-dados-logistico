import src.app.visualizacoes.uteis.graficos as graf
from src.app.controles.financeiro.modelo_dados import ControleDadosSaida
from src.app.uteis.formatar_unidades import formatar_valores_monetarios
from src.app.visualizacoes.uteis.cores_graf_barras import estilizar_cor_grafico_barras

from ....uteis.graficos import GraficoDadosEntrada
from ...uteis.nomes_dos_graficos import NomeGraficos
from .dados_customizados_barra import dados_customizados
from .dica_graficos import dica_graf_coluna


def graf_barra(dados_controle: ControleDadosSaida, dados_grafico: GraficoDadosEntrada):
    customizados = dados_customizados(dados_controle, dados_grafico.nome)
    dica = __fluxo_dica_ferramenta(dados_grafico.nome)
    rotulo = formatar_valores_monetarios(dados_controle.eixo_y, 1)
    cores = estilizar_cor_grafico_barras(dados_grafico.cor, dados_grafico.cor_alerta, dados_controle.indicadores)
    return graf.colunas(dados_grafico, rotulo, cores, customizados, dica, posicao_rotulo="outside")


def __fluxo_dica_ferramenta(nome_grafico: NomeGraficos) -> str:
    if nome_grafico == NomeGraficos.RECEITA:
        return dica_graf_coluna(nome_grafico.value, NomeGraficos.META.value)
    return dica_graf_coluna(nome_grafico.value, NomeGraficos.LIMITE_CUSTO.value)
