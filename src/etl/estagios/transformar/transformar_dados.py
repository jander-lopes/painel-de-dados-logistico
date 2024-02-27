from .feriados.feriados import dados_feriados
from .financeiro.analise_financeira import dados_para_analise_financeira
from .metas.metas import dados_metas


def estagio_transformar():
    print("\nEstágio Transformar Inicilizada\n")
    dados_para_analise_financeira()
    dados_metas()
    dados_feriados()
    print("\nEstágio Transformar Finalizado\n")
