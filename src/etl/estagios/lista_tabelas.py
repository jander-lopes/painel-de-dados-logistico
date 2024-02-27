from .modelo_dados.dados_extracao import DadosEstagioExtracao


def dados_para_estagio_extracao():
    return [
        DadosEstagioExtracao("fretes", "relatorio_cargas", 2),
        DadosEstagioExtracao("custos", "custos_mensais", 0),
        DadosEstagioExtracao("ocorrencias", "motivos_ocorrencia", 0),
        DadosEstagioExtracao("veiculos", "cadastro_veiculo", 0),
    ]
