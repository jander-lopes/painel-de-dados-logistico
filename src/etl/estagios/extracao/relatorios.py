from ..modelo_dados.dados_extracao import DadosEstagioExtracao


def relatorios():
    return [
        DadosEstagioExtracao("fretes", "relatorio_cargas", 2),
        DadosEstagioExtracao("custos", "custos_mensais"),
        DadosEstagioExtracao("ocorrencias", "motivos_ocorrencia"),
        DadosEstagioExtracao("veiculos", "cadastro_veiculo"),
        DadosEstagioExtracao("metas", "metas"),
        DadosEstagioExtracao("feriados", "feriados_nacionais"),
    ]
