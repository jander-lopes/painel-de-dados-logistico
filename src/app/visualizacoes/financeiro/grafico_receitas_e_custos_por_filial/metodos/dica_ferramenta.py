from pandas import Series

from ...uteis.nomes_dos_graficos import NomeGraficos


def dica_ferramenta(nome_grafico: NomeGraficos) -> str:
    if nome_grafico == NomeGraficos.RECEITA:
        return __mensagem_dica_ferramentas("%{text}", "%{customdata[0]}")
    return __mensagem_dica_ferramentas("%{customdata[0]}", "%{text}")


def __mensagem_dica_ferramentas(receitas: str, custos: str) -> str:
    return (
        "<b style='font-size: 1rem'>%{y}</b><br><br>"
        + f"<span style='font-size: 1rem'>Receitas =</span> <b style='font-size: 1rem'> R$ {receitas}</b><br>"
        + f"<span style='font-size: 1rem'>Custos =</span> <b style='font-size: 1rem'> R$ {custos}</b><br><br>"
        + "<span style='font-size: 1rem'>Resultado =</span> <b style='font-size: 1rem'> R$ %{customdata[1]}</b><br><br>"
        + "<span style='font-size: 1rem'>Limite de custos =</span> <b style='font-size: 1rem'>70% da receita</b><br><br>"
        + "%{customdata[2]}",
    )


def dica_limite_de_custos(valores: Series) -> list[str]:
    return [
        (
            __mensagem_limite_custos(valor, "abaixo", "green")
            if valor < 0
            else __mensagem_limite_custos(valor, "acima", "red")
        )
        for valor in valores
    ]


def __mensagem_limite_custos(valor: int | float, posicao: str, cor: str) -> str:
    return f"<span style='font-size: 1rem'>Os custos estão  <b style='color: {cor}'>{abs(valor):.0f}%</b>  {posicao} do limite de custos</span>"
