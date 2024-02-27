import src.app.infra.bd.tabelas as tb


def feriados_cidade_sp(ano: int) -> list[str]:
    feriados = tb.tb_feriados()
    feriados_municipais_sp = [f"{ano}-01-25", f"{ano}-07-09", f"{ano}-11-20"]
    feriados_por_ano = feriados.query(f"data.dt.year == {ano}")
    return sorted(
        [
            *feriados_municipais_sp,
            *feriados_por_ano.data.dt.strftime("%Y-%m-%d").to_list(),
        ]
    )
