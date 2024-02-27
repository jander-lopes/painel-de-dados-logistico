from pandas import Series


def taxa_cumprimento_meta_receitas(taxas: Series, casas_decimais: int = 0):
    if taxas.empty:
        return taxas
    mensagens = __mensagens_receitas()
    return __lista_de_mensagens(taxas, mensagens, casas_decimais)


def taxa_cumprimento_meta_custos(taxas: Series, casas_decimais: int = 0):
    if taxas.empty:
        return taxas
    mensagens = __mensagens_custos()
    return __lista_de_mensagens(taxas, mensagens, casas_decimais)


def __lista_de_mensagens(taxas: Series, mensagens: dict, casas_decimais: int):
    resposta = []
    for valor in taxas.to_list():
        mensagem = __definir_mensagem(round(valor, casas_decimais), mensagens, casas_decimais)
        resposta.append(mensagem)
    return resposta


def __definir_mensagem(valor: int | float, mensagens: str, casas_decimais: int):
    match valor:
        case valor if valor > 0:
            return __mensagem(valor, mensagens["acima"], casas_decimais)
        case valor if valor < 0:
            return __mensagem(valor, mensagens["abaixo"], casas_decimais)
        case _:
            return __mensagem(valor, mensagens["neutro"], casas_decimais)


def __mensagem(valor: int | float, dados: dict[str, str], casas_decimais: int) -> str:
    return f"<span style='font-size: 1rem'><b style='color: {dados['cor']}; font-size: 1rem'>{dados['simbolo']}{abs(valor):.{casas_decimais}f}%</b> {dados['mensagem']}</span>"


# SIMBOLOS
# SETA PARA CIMA -> \u2191
# SETA PARA BAIXO -> \u2193
def __mensagens_receitas() -> dict[dict[str, str]]:
    return dict(
        acima=dict(cor="green", simbolo="\u2191", mensagem="acima da meta"),
        abaixo=dict(cor="red", simbolo="\u2193", mensagem="abaixo da meta"),
        neutro=dict(cor="", simbolo="", mensagem="meta atingida"),
    )


def __mensagens_custos() -> dict[dict[str, str]]:
    return dict(
        acima=dict(cor="red", simbolo="\u2191", mensagem="acima do limite de custos"),
        abaixo=dict(cor="green", simbolo="\u2193", mensagem="abaixo do limite de custos"),
        neutro=dict(cor="", simbolo="", mensagem="atingiu o limite de custos"),
    )
