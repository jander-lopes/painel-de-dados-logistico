import datetime as dt

import pandas as pd

import src.congifuracao.diretorios as diretorio

from ..modelo_dados.dados_extracao import DadosEstagioExtracao
from ..uteis.fazer_backup_arquivo import fazer_backup
from ..uteis.listar_arquivos import listar_arquivos
from .relatorios import relatorios


def estagio_extracao() -> None:
    print("\nEstágio Extrair Inicializado\n")
    for relatorio in relatorios():
        if relatorio.arquivo.is_file():
            __atualizar_relatorio(relatorio)
        else:
            __extrair_todos_relatorios(relatorio)
    print("\nEstágio Extrair Finalizado\n")


def __extrair_todos_relatorios(entrada: DadosEstagioExtracao) -> None:
    arquivos = listar_arquivos(diretorio.BD_RELATORIOS / entrada.pasta, "csv")
    dataframes = []
    for arquivo in arquivos:
        dataframes.append(pd.read_csv(arquivo, header=entrada.linha_cabecalho, sep=";"))
        print(f"Carregar: {arquivo.name} -> OK -> Data: {dt.datetime.now().isoformat()}")
    if dataframes:
        df = pd.concat(dataframes, ignore_index=True)
        df.to_parquet(entrada.arquivo)
    print(f"Salvar: {entrada.arquivo.name} -> OK -> Data: {dt.datetime.now().isoformat()}")


def __atualizar_relatorio(entrada: DadosEstagioExtracao) -> None:
    dados_atuais = pd.read_parquet(entrada.arquivo)
    dados_bd = pd.read_csv(entrada.arquivo_bd, header=entrada.linha_cabecalho, sep=";")
    dados_atualizados = (
        dados_atuais.merge(dados_bd, on=list(dados_atuais), how="outer")
        .drop_duplicates(keep="last")
        .reset_index(drop=True)
    )
    fazer_backup(entrada.arquivo, entrada.backup, diretorio.EXTRACAO_PASTA_BACKUP, entrada.nome_arquivo)
    dados_atualizados.to_parquet(entrada.arquivo, index=False)
    print(
        f"Carregar: {entrada.arquivo_bd.name} -> Atualizar: {entrada.arquivo.name} -> OK -> Data: {dt.datetime.now().isoformat()}"
    )
