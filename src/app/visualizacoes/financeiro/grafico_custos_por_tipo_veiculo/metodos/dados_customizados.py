from src.app.controles.financeiro.custos_por_tipo_veiculo import ControleDadosSaida
from src.app.uteis.formatar_unidades import formatar_valores_monetarios


def dados_customizados(entrada: ControleDadosSaida) -> None:
    return (
        entrada.tipo_veiculo,
        formatar_valores_monetarios(entrada.abastecimento),
        entrada.repre_abastecimento,
        formatar_valores_monetarios(entrada.manutencao),
        entrada.repre_manutencao,
        formatar_valores_monetarios(entrada.fixos),
        entrada.repre_fixos,
        formatar_valores_monetarios(entrada.custos),
        entrada.repre_custo,
    )
