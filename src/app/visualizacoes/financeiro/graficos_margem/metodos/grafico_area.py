import src.app.configuracao.cores as cor
from src.app.controles.financeiro.margem_meses import ControleDadosSaida
from src.app.visualizacoes.uteis.graficos import DadosGraficoArea


def grafico_de_area(dados: ControleDadosSaida) -> DadosGraficoArea:
    return DadosGraficoArea(
        name="Margem",
        x=dados.eixo_x,
        y=dados.eixo_y,
        text=dados.eixo_y,
        mode="lines+markers+text",
        texttemplate="%{text:.0f}%",
        line=dict(color=cor.margem, dash="dash"),
        fillcolor=cor.area,
        hovertemplate="<b style='font-size: 1rem'>%{text:.0f}%</b>",
    )
