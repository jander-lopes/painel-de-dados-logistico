def dica_graf_coluna(descricao_medida: str, descricao_meta: str) -> str:
    return (
        "<span style='font-size: 1rem'><b>"
        + descricao_medida
        + ":</b> %{customdata[0]}</span><br>"
        + "<span style='font-size: 1rem'><b>"
        + descricao_meta
        + ":</b> %{customdata[1]}</span><br><br>"
        + "%{customdata[2]}"
    )


def dica_graf_linha(descricao_medida: str):
    return "<b style='font-size: 1rem;'>" + descricao_medida + ": %{customdata}</b>"
