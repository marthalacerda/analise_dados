"""Executa o programa principal
Fluxo:
1. Extrair dados do banco de dados para a lista de entrada
2. Pedir ao usuário a opção de API para inferir gênero
3. Instanciar classes de controle
4. Iterar lista de entrada:
    Instanstanciar e tratar Pessoa
    Adicionar na lista de saída
5. Salvar arquivo json
6. Analisar os dados
"""

from pathlib import Path
import pandas as pd
from src.services.conexao_service import tem_conexao
from src.repo import csv_repo
from src.repo import json_repo
from src.controllers.pessoa_controller import PessoaController
import src.reports.relatorio_service as relatorio


# Definindo o caminho do arquivo de entrada
CAMINHO_CSV = Path('data/lista_clientes.csv')


# Função de execução principal
def main():
    """Executa o programa"""

    # Testando conexão com a internet
    if not tem_conexao():
        print()
        print('=' * 60)
        print('Sem conexão com a internet'.center(60))
        print('=' * 60)
        return

    exibir_cabecalho()
    opcao = escolher_api_genero()

    if opcao == '0':
        print()
        print('=' * 60)
        print('Programa encerrado'.center(60))
        print('=' * 60)
        return

    print('\n- - - Processando - - -')

    # Listas de entrada e saidaa
    lista_clientes = csv_repo.ler_csv(CAMINHO_CSV)
    lista_saida = []

    # Criar controlador
    controller = PessoaController(opcao)

    for pessoa in lista_clientes:

        # Instanciando Pessoa
        cliente = controller.construir_pessoa(pessoa)

        # Adicionando na lista de saida
        lista_saida.append(controller.to_dict(cliente))

    # Analisando e imprimindo os dados de saída
    data_frame = pd.DataFrame(lista_saida)
    print('=' * 60)
    print('Relatório de Saída'.center(60))
    print('=' * 60)
    relatorio.genero_report(data_frame)
    print('-' * 60)
    relatorio.regiao_report(data_frame)
    print('-' * 60)
    relatorio.qualidade_report(data_frame)
    print('-' * 60)
    relatorio.interesses_report(data_frame)
    print('-' * 60)
    relatorio.top_interesses_gen(data_frame)
    print('-' * 60)

    # Gerando arquivo de saída
    json_repo.salvar_json(lista_saida)


def exibir_cabecalho() -> None:
    """Imprime cabeçalho do programa"""
    print('=' * 60)
    print('SISTEMA DE ANÁLISE DE DADOS DE CLIENTES'.center(60))
    print('Leitura, validação e enriquecimento de dados'.center(60))
    print('=' * 60)
    print()


def escolher_api_genero() -> str:
    """Pede ao usuário para escolher a API para inferência de genero
    1) genderize.io
    2) genderapi.io
    3) gender-api.com

    Retorna:
        str: Escolha do usuário
    """
    print('Escolha o serviço para inferir o gênero dos clientes:')
    print('1 - Genderize.io\n2 - GenderAPI.io\n3 - Gender-API.com\n4 - Nenhum\n0 - Sair')
    while True:
        escolha = input('Digite opção: ')
        if escolha in ('1', '2', '3', '4', '0'):
            return escolha
        print('⚠  Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
