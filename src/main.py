"""Módulo que executa o programa
Fluxo:
1. Extrair dados do banco de dados para a lista de entrada
2. Pedir ao usuário a opção de API para inferir gênero
3. Instanciar classes de controle
4. Iterar lista de entrada:
    Instanstanciar e tratar Pessoa
    Adicionar na lista de saída
5. Salvar arquivo json
"""
from pathlib import Path


# Repositórios
from src.repo import csv_repo
from src.repo import json_repo

# Controladores
from src.controllers.pessoa_controller import PessoaController



# Definindo o caminho do arquivo de entrada
CAMINHO_CSV = Path('data/lista_clientes.csv')




# Função de execução principal
def main():
    """Executa o programa"""

    # Listas de entrada e saidaa
    lista_clientes = csv_repo.ler_csv(CAMINHO_CSV)
    lista_saida = []

    exibir_cabecalho()
    opcao = escolher_api_genero()

    if opcao == '0':
        return

    # Criar controlador
    controller = PessoaController(opcao)


    # Iterando lista de clientes
    for pessoa in lista_clientes:

        # Instanciando Pessoa
        cliente = controller.construir_pessoa(pessoa)

        # Adicionando na lista de saida
        lista_saida.append(controller.to_dict(cliente))
    
    print(lista_saida)
    
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
    print('1 - Genderize.io\n2 - GenderAPI.io\n3 - Gender-API.com\n0 - Sair')
    while True:
        escolha = input('Digite opção: ')
        if escolha in ('1', '2', '3', '0'):
            return escolha
        print('⚠  Opção inválida. Tente novamente.')






if __name__ == '__main__':
    main()


# Criando o conteudo do arquivo - .to_dict() monta a estrutura de Pessoa
# dados = [pessoa.to_dict() for pessoa in lista_pessoas]
