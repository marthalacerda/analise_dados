"""
Módulo da classe PessoaController
Esta classe tem todos os métodos necessários para o fluxo de criação do objeto Pessoa
Lista de métodos:

.criar_endereco(cep)
.formatar_celular(cel)

"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pathlib import Path
from src.repo.csv_repo import ler_csv
from src.models.pessoa import Pessoa
from src.models.endereco import Endereco
from src.services import cep_service
from src.models.cpf import CPF

# depois mudar - tirar os src. e apagar as 3 primeiras linhas lá de cima

class PessoaController:
    """Classe com métodos para a montagem de objeto Pessoa"""
    



#-------------------------------------------------------





def construir_pessoa(dados_pessoa: dict) -> Pessoa:
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
        pessoa.endereco = formatar_celular(pessoa)      # aqui ajustou o celular
    except ValueError as e:
        pessoa.observacoes.append(e)

    # Chamar init de CPF para validar o cpf de Pessoa
    try:
        CPF(pessoa.cpf)                         # aqui a instancia de CPF verificou o cpf
    except ValueError as e:
        pessoa.observacoes.append(e)




    # Atribuir as informações de endereço em Pessoa
    # pessoa.atribuir_endereco(endereco)          # aqui criou o atributo endereco em Pessoa
    # pessoa.bairro = endereco.bairro
    # pessoa.cidade = endereco.cidade
    # pessoa.estado = endereco.estado
    # pessoa.endereco = endereco



# Criando Endereço da Pessoa
def criar_endereco(pessoa: Pessoa) -> Endereco:
    """Função que busca as informações do cep via API e cria endereço.
    
    Argumentos:
        pessoa (Pessoa): Objeto Pessoa que vai fornecer o cep

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
    cel = pessoa.celular

    cel_so_numeros = ''.join(filter(lambda x: x.isdigit(), cel))

    # Verificando
    if not cel_so_numeros:
        pessoa.observacoes.append('Celular com campo vazio.')
        # raise ValueError('Celular com campo vazio.')

    elif 8 > len(cel_so_numeros) > 0 or len(cel_so_numeros) > 11:
        pessoa.observacoes.append('Celular inválido.')
        # raise ValueError('Celular inválido.')
    
    elif len(cel_so_numeros) > 8 and cel_so_numeros[-9] != '9':
        pessoa.observacoes.append('Celular Inválido.')
        # raise ValueError('Celular inválido.')
    
    
    if len(cel_so_numeros) == 8:
        cel = f'{pessoa.endereco.ddd} 9{cel_so_numeros}'
    elif len(cel_so_numeros) == 9:
        cel = f'{pessoa.endereco.ddd} {cel_so_numeros}'
    elif len(cel_so_numeros) == 10:
        cel = f'{cel_so_numeros[:2]} 9{cel_so_numeros[2:]}'
    elif len(cel_so_numeros) == 11:
        cel = f'{cel_so_numeros[:2]} {cel_so_numeros[2:]}'

    return cel

        

    

       










# Testes

# Ler o arquivo CSV e colocar dados numa lista de dicionarios
lista_clientes = ler_csv(Path(__file__).resolve().parent.parent.parent\
                        /"data"/"lista_clientes.csv")

# Criando instancia de Pessoa com a primeira posição da lista do arquivo
pessoa1 = Pessoa(lista_clientes[0])

# testando retornos de funções ... em andamento
print('----------Testes-----------')
print('Nome completo:', pessoa1.nome_completo)
print('Primeiro nome:', pessoa1.primeiro_nome)
print('Segundo nome:', pessoa1.segundo_nome)

end = criar_endereco(pessoa1)
print(end.__dict__)
print()
pessoa1.endereco = end
# pessoa1.atribuir_endereco(end)
print(pessoa1.endereco.bairro)
print()
print(pessoa1.celular)
formatar_celular(pessoa1)
print(pessoa1.celular)
print()
print(pessoa1.observacoes)
print()
print(pessoa1.__dict__)
print()

print(pessoa1.cpf)
print()