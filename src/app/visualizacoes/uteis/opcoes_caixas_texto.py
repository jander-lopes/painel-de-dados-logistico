import src.app.infra.repositorio.financeiro.consultas as repo


def opcoes_anos() -> list[str]:
    return repo.lista_anos()


def opcoes_meses(ano: int) -> list[str]:
    return repo.lista_meses(ano)


def opcoes_filiais(ano: int) -> list[str]:
    return repo.lista_filiais(ano)
