from ..modelo_dados.dados_extracao import DadosEstagioExtracao
from .listar_arquivos import listar_arquivos


def arquivos_faltantes(tabela: DadosEstagioExtracao):
    arquivos_bd = listar_arquivos(tabela.arquivo_bd.parent, tabela.arquivo_bd.suffix)
    arquivos_extracao = listar_arquivos(tabela.arquivo_extracao.parent, tabela.arquivo_extracao.suffix)
    nomes_bd = {arquivo.stem for arquivo in arquivos_bd}
    nomes_extracao = {arquivo.stem for arquivo in arquivos_extracao}
    arquivos_faltantes = nomes_bd - nomes_extracao
    return [arquivo for arquivo in arquivos_bd if arquivo.stem in arquivos_faltantes]
