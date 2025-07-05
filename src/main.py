"""Módulo onde se instancia as classes"""

from pathlib import Path
from models.pessoa import Pessoa
from repo.csv_repo import ler_csv

# Ler o arquivo CSV e colocar dados numa lista de dicionarios
lista_clientes = ler_csv(Path(__file__).resolve().parent.parent / "data" / "lista_clientes.csv")


# Criando instancia de Pessoa com a primeira posição da lista do arquivo
pessoa1 = Pessoa(lista_clientes[0])

# testando retornos de funções ... em andamento
print(pessoa1.ler_nome())
print(pessoa1.nome_completo)
print(pessoa1.primeiro_nome)
print(pessoa1.segundo_nome)
print(pessoa1.formatar_cep())



