from dataclasses import dataclass

from src.app.controles.financeiro.metricas import ControleDadosSaida, DadosIndicadores, controle
from src.app.infra.repositorio.modelo_dados import DadosRequisicao
from src.app.uteis.formatar_unidades import formatar_moeda, formatar_percentil


@dataclass
class Indicadores:
    receita: str | None = None
    custo: str | None = None
    resultado: str | None = None
    margem: str | None = None


@dataclass
class DadosMetricas:
    receita: str
    custo: str
    resultado: str
    margem: str
    indicador: Indicadores


def resposta(requisicao: DadosRequisicao) -> DadosMetricas:
    dados = controle(requisicao)
    return __formatar_dados(dados)


def __formatar_dados(dados: ControleDadosSaida) -> DadosMetricas:
    indicadores = __formatar_indicadores(dados.indicador) if dados.indicador.receita else Indicadores()
    return DadosMetricas(
        formatar_moeda(dados.receita, 1),
        formatar_moeda(dados.custo, 1),
        formatar_moeda(dados.resultado, 1),
        formatar_percentil(dados.margem, 0),
        indicadores,
    )


def __formatar_indicadores(indicador: DadosIndicadores) -> None:
    return Indicadores(
        formatar_percentil(indicador.receita, 0),
        formatar_percentil(indicador.custo, 0),
        formatar_percentil(indicador.resultado, 0),
        formatar_percentil(indicador.margem, 0),
    )
