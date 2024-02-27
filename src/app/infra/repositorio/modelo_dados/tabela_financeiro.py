from dataclasses import dataclass


@dataclass
class DadosRequisicao:
    ano: int
    num_mes: int | None = None
    filial: str | None = None
    mes: str | None = None


@dataclass
class AtributosTabelaAnaliseFinanceira:
    ano: str = "ano"
    num_mes: str = "num_mes"
    mes: str = "mes"
    filial: str = "filial"
    tipo_veiculo: str = "tipo_veiculo"
    carroceria: str = "carroceria"
    qnt_pedidos: str = "qnt_pedidos"
    receitas: str = "receitas"
    abastecimento: str = "abastecimento"
    manutencao: str = "manutencao"
    custo_fixo: str = "custo_fixo"
    custos: str = "custos"


@dataclass
class AtributosTabelaMetas:
    ano: str = "ano"
    receitas: str = "metas_receitas"


@dataclass
class Medidas:
    resultado: str = "resultado"
    ticket_medio: str = "ticket_medio"
    margem: str = "margem"
