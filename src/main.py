"""Módulo onde se instancia as classes"""

from pathlib import Path
from models.endereco import Endereco
from models.pessoa import Pessoa
from repo.csv_repo import ler_csv
from services import cep_service

# Ler o arquivo CSV e colocar dados numa lista de dicionarios
lista_clientes = ler_csv(Path(__file__).resolve().parent.parent / "data" / "lista_clientes.csv")


# Criando instancia de Pessoa com a primeira posição da lista do arquivo
pessoa1 = Pessoa(lista_clientes[0])

# testando retornos de funções ... em andamento
print('----------Testes-----------')
print('Nome completo:', pessoa1.nome_completo)
print('Primeiro nome:', pessoa1.primeiro_nome)
print('Segundo nome:', pessoa1.segundo_nome)

# Criando Endereço da Pessoa
pessoa1_cep = pessoa1.ler_cep()
dados_cep = cep_service.buscar_cep(pessoa1_cep)
endereco = Endereco(dados_cep)

print(endereco.__dict__)