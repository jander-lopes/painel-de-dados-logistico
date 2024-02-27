# Outra forma de formatar moedas
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
# valor_formatado = locale.currency(valor_a_ser_formatado, grouping=True, symbol=True)

from enum import Enum

import pandas as pd

DataFrame = pd.DataFrame


class Unidade(Enum):
    NENHUM = 1
    Mil = 1000
    Mi = 1_000_000
    Bi = 1_000_000_000
    Tri = 1_000_000_000_000


class Formatar(Enum):
    moeda = "moeda"
    porcentagem = "porcentagem"


def formatar_valores_monetarios(valores: pd.Series, casas_decimais: int = 0, simbolo_moeda: str = ""):
    if valores.empty:
        return valores
    return valores.apply(lambda valor: formatar_moeda(valor, casas_decimais, simbolo_moeda))


def formatar_moeda(valor: int | float, casas_decimais: int, simbolo_moeda: str = ""):
    unidade = __definir_unidade(abs(valor))
    nome_unidade = "" if unidade.name == "NENHUM" else unidade.name
    novo_valor = valor / unidade.value
    return f"{simbolo_moeda} {novo_valor:_.{casas_decimais}f} {nome_unidade}".replace(".", ",").replace("_", ".")


def formatar_valores_percentil(valores: pd.Series, casas_decimais: int = 0) -> pd.Series:
    if valores.empty:
        return valores
    return valores.apply(lambda valor: formatar_percentil(valor, casas_decimais))


def formatar_percentil(valor: float, casas_decimais: int = 0):
    return f"{valor:_.{casas_decimais}f} %".replace(".", ",").replace("_", ".")


def __definir_unidade(valor: int | float) -> Unidade:
    match valor:
        case valor if valor < 1e3:
            return Unidade.NENHUM
        case valor if valor < 1e6:
            return Unidade.Mil
        case valor if valor < 1e9:
            return Unidade.Mi
        case valor if valor < 1e12:
            return Unidade.Bi
        case _:
            return Unidade.Tri
