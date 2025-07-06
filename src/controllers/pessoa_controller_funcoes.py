"""
Módulo da classe PessoaController
Esta classe tem todos os métodos necessários para o fluxo de criação do objeto Pessoa

Fluxo:
1. Instanciar Pessoa com dados brutos do Banco de Dados
2. Instanciar Endereco através do CEP
3. Formatar celular baseando no ddd
4. Validar CPF
5. Inferir o gênero
6. Retornar Pessoa com dados completos
"""

import sys
import os

# 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pathlib import Path
from src.repo.csv_repo import ler_csv
from src.models.pessoa import Pessoa
from src.models.endereco import Endereco
from src.services import cep_service, gender_service
from src.models.cpf import CPF

# depois mudar - tirar os src. e apagar as 3 primeiras linhas lá de cima

class PessoaController:
    """Classe com métodos para a montagem de objeto Pessoa
    Faz o controle do fluxo de criação, chamando todos os métodos
    para obter as informações necessárias para completar o objeto Pessoa.
    
    Parâmetros:
        opcao_genero (str): Escolha do usuário para a API que vai inferir o gênero de Pessa."""

    def __init__(self, opcao_genero):
        """Inicia o Controller"""
        ...



#-------------------------------------------------------





def construir_pessoa(dados_pessoa: dict, opcao_genero) -> Pessoa:
    """Função para construir uma instância de Pessoa.
    
    Argumentos:
        dados_pessoa: Dicionário com as informações do cliente no banco de dados
    
    Retorna:
        Pessoa: Instância de Pessoa
    """

    # Criar Pessoa com atributos semi preenchidos
    pessoa = Pessoa(dados_pessoa)           # aqui tratou e atribuiu os nomes

    # Criar Endereco atraves do CEP da pessoa e atribuir a ela
    try:
        pessoa.endereco = criar_endereco(pessoa)     # aqui criou endereço
    except (ValueError, ConnectionError) as e:
        print(e)

    # Ler o telefone e verificar se é válido ou se precisa de ajuste
    try:
        pessoa.celular = formatar_celular(pessoa)      # aqui ajustou o celular
    except ValueError as e:
        pessoa.add_observacao(str(e))

    # Chamar init de CPF para validar o cpf de Pessoa
    try:
        CPF(pessoa.cpf)                         # aqui a instancia de CPF verificou o cpf
    except ValueError as e:
        pessoa.add_observacao(str(e))

    # Acessar API de genero
    try:
        pessoa.genero = buscar_genero(pessoa, opcao_genero)     # aqui acessou api de genero e atribuiu
    except ConnectionError as e:
        print(e)

    return pessoa


# Criando CEP e validando
def validar_cpf(pessoa: Pessoa) -> None:
    """Instancia CPF com o cpf da Pessoa e faz a validação
    
    Argumentos:
        pessoa (Pessoa): Objeto Pessoa que terá o cpf validado
    
    Levanta:
        ValueError: Caso o CPF seja inválido.
    """
    cpf = pessoa.cpf
    CPF(cpf)


# Criando Endereço da Pessoa
def criar_endereco(pessoa: Pessoa) -> Endereco:
    """Função que busca as informações do cep via API e cria endereço.
    
    Argumentos:
        pessoa (Pessoa): Objeto Pessoa que vai fornecer o cep

    Levanta:
        ValueError: CEP não encontrado
        ConnectionError: Erro na conexão com a API

    Retorna:
        Endereco: Instância da classe Endereco
    """
    cep = pessoa.ler_cep()

    # Buscar os dados do CEP
    dados_cep = cep_service.buscar_cep(cep)

    # Retornar instancia de endereço
    return Endereco(dados_cep)


# Validando celular da Pessoa
def formatar_celular(pessoa: Pessoa) -> str:
    """Ajeita o número do celular na formação dos requisitos.
    'DD 9XXXXXXXX'
    
    Argumentos:
        pessoa (Pessoa): Objeto Pessoa que sofrerá a formatação do celular
    
    Retorna:
        str: Celular formatado
    """
    # cel = pessoa.celular
    # Filtrar o celular para ficar com somente números
    cel = ''.join(filter(lambda x: x.isdigit(), pessoa.celular))

    # Verificando
    if not cel:
        # pessoa.observacoes.append('Celular com campo vazio.')
        raise ValueError('Celular com campo vazio.')

    elif 8 > len(cel) > 0 or len(cel) > 11:
        # pessoa.observacoes.append('Celular inválido.')
        raise ValueError('Celular inválido.')
    
    elif len(cel) > 8 and cel[-9] != '9':
        # pessoa.observacoes.append('Celular Inválido.')
        raise ValueError('Celular inválido.')
        
    if len(cel) == 8:
        cel = f'{pessoa.endereco.ddd} 9{cel}'
    elif len(cel) == 9:
        cel = f'{pessoa.endereco.ddd} {cel}'
    elif len(cel) == 10:
        cel = f'{cel[:2]} 9{cel[2:]}'
    elif len(cel) == 11:
        cel = f'{cel[:2]} {cel[2:]}'

    return cel


def buscar_genero(pessoa: Pessoa, opcao: str) -> str:
    """Acessa API para inferir o gênero de Pessoa
    
    Argumentos:
        pessoa (Pessoa): Objeto Pessoa que vai fornecer o nome
        opcao (str): Escolha do usuário (coletada em tempo de execução)

    Levanta:
        ConnentionError: Caso tenha erro na conexão com a API 
        
    Retorna:
        str: Genero da pessoa (male/female)
    """
    nome = pessoa.primeiro_nome
    genero = ''

    # Chamar a função da API escolhida pelo usuário
    match opcao:
        case '1':
            genero = gender_service.buscar_genderize(nome)

        case '2':
            genero = gender_service.buscar_genderapi(nome)

        case '3':
            genero = gender_service.buscar_genderapicom(nome)

    return genero
    

       










# Testes

# Ler o arquivo CSV e colocar dados numa lista de dicionarios
lista_clientes = ler_csv(Path(__file__).resolve().parent.parent.parent\
                        /"data"/"lista_clientes.csv")

# Criando instancia de Pessoa com a primeira posição da lista do arquivo
# pessoa1 = Pessoa(lista_clientes[0])

print(lista_clientes[0])
print()
pessoa2 = construir_pessoa(lista_clientes[0], '')

print(pessoa2.observacoes)
print(pessoa2.__dict__)





# # testando retornos de funções ... em andamento
# print('----------Testes-----------')
# print('Nome completo:', pessoa1.nome_completo)
# print('Primeiro nome:', pessoa1.primeiro_nome)
# print('Segundo nome:', pessoa1.segundo_nome)

# end = criar_endereco(pessoa1)
# print(end.__dict__)
# print()
# pessoa1.endereco = end
# # pessoa1.atribuir_endereco(end)
# print(pessoa1.endereco.bairro)
# print()
# print(pessoa1.celular)
# formatar_celular(pessoa1)
# print(pessoa1.celular)
# print()
# print(pessoa1.observacoes)
# print()
# print(pessoa1.__dict__)
# print()

# print(pessoa1.cpf)
# print()

# #validar_cpf(pessoa1)
# print(pessoa1.observacoes)

