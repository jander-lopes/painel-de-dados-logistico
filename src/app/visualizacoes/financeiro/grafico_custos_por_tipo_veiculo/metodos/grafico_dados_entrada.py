from pandas import Series

from src.app.controles.financeiro.custos_por_tipo_veiculo import ControleDadosSaida

from ....uteis.graficos import GraficoDadosEntrada
from ...uteis.nomes_dos_graficos import NomeGraficos


def dados_grafico(entrada: ControleDadosSaida, nome_grafico: NomeGraficos, cor: str) -> GraficoDadosEntrada:
    eixo_x = __eixo_x(entrada, nome_grafico)
    return GraficoDadosEntrada(eixo_x, entrada.tipo_veiculo, nome_grafico, cor)


def __eixo_x(entrada: ControleDadosSaida, nome_grafico: NomeGraficos) -> Series:
    eixos = __valores_eixos(entrada)
    return eixos[nome_grafico]


def __valores_eixos(entrada: ControleDadosSaida) -> dict[NomeGraficos, Series]:
    return {
        NomeGraficos.ABASTECIMENTO: entrada.abastecimento,
        NomeGraficos.MANUTENCAO: entrada.manutencao,
        NomeGraficos.CUSTOS_FIXOS: entrada.fixos,
    }
