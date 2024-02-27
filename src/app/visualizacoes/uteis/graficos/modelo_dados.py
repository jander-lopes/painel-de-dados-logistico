from dataclasses import dataclass

from pandas import Series

from ...financeiro.uteis.nomes_dos_graficos import NomeGraficos


@dataclass
class GraficoDadosEntrada:
    eixo_x: Series
    eixo_y: Series
    nome: NomeGraficos
    cor: str
    cor_alerta: str | None = None
    xaxis: str | None = None
