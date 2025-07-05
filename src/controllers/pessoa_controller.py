import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pathlib import Path
from src.repo.csv_repo import ler_csv
from src.models.pessoa import Pessoa
from src.models.endereco import Endereco
from src.services import cep_service

# depois mudar - tirar os src. e apagar as 3 primeiras linhas lá de cima

def construir_pessoa(dados_pessoa: dict) -> Pessoa:
    """Função para construir uma instância de Pessoa.
    
    Args:
    
    Returns:
        Pessoa: Instância de Pessoa
    """
    
    # Criar Pessoa com dados incompletos
    pessoa = Pessoa(dados_pessoa)           # aqui tratou e atribuiu os nomes

    # Criar Endereco atraves do CEP da pessoa
    endereco = criar_endereco(pessoa.ler_cep())     # aqui criou endereço

    # Atribuir as informações de endereço em Pessoa
    pessoa.atribuir_endereco(endereco)
    # pessoa.bairro = endereco.bairro
    # pessoa.cidade = endereco.cidade
    # pessoa.estado = endereco.estado
    






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

# Criando Endereço da Pessoa
def criar_endereco(cep: str) -> Endereco:
    """Função que busca as informações do cep via API e cria endereço.
    
    Args:
        cep (str): Código de Endereçamento Postal

    Returns:
        Endereco: Instância da classe Endereco
    """
    # Buscar os dados do CEP
    dados_cep = cep_service.buscar_cep(cep)

    # Retornar instancia de endereço
    return Endereco(dados_cep)

end = criar_endereco(pessoa1.ler_cep())
print(end.__dict__)
print()
pessoa1.atribuir_endereco(end)
print(pessoa1.endereco.bairro)