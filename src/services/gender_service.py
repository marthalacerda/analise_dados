"""
Módulo para fazer requisição às APIs generize.io, genderapi.io e gender-api.com
Nese módulo estão implementadas funções de cada requisição
"""

import requests

# API Genderize.io
def buscar_genderize(nome: str) -> str:
    """Faz a requisição get à API Genderize.io retorna os dados do nome
    
    Argumentos:
        nome (str): Primeiro nome de Pessoa

    Levanta:
        ConnectionError: Caso não seja possível a comunicação com a API.
    
    Retorna:
        str: Genero provável do nome (male/female)
    """

    # Definindo a url da requisição get à API genderize.io
    url = f'https://api.genderize.io?name={nome}&country_id=BR'

    # Fazendo a requisição
    resposta = requests.get(url, timeout=5)

    # Verificando o status da requisição
    if resposta.status_code != 200:
        raise ConnectionError('Erro ao conectar com a API Genderize.io.')
    
    # Pegar os dados em formato JSON
    dados_nome = resposta.json()

    return dados_nome.get('gender')

# API GenderAPI.io
def buscar_genderapi(nome: str) -> str:
    """Faz a requisição get à API GenderAPI.io retorna os dados do nome
    
    Argumentos:
        nome (str): Primeiro nome de Pessoa

    Levanta:
        ConnectionError: Caso não seja possível a comunicação com a API.
    
    Retorna:
        str: Genero provável do nome (male/female)
    """
    key = '686a20f6e57908da4dbe6f58'

    # Definindo a url da requisição get à API GenerAPI.io
    url = f'https://api.genderapi.io/api/?name={nome}&key={key}'

    # Fazendo a requisição
    resposta = requests.get(url, timeout=5)

    # Verificando o status da requisição
    if resposta.status_code != 200:
        raise ConnectionError('Erro ao conectar com a API GenderAPI.io.')
    
    # Pegar os dados em formato JSON
    dados_nome = resposta.json()

    return dados_nome.get('gender')

# API Gender-API.com
def buscar_genderapicom(nome: str) -> str:
    """Faz a requisição get à API Gender-API.com retorna os dados do nome
    
    Argumentos:
        nome (str): Primeiro nome de Pessoa

    Levanta:
        ConnectionError: Caso não seja possível a comunicação com a API.
    
    Retorna:
        str: Genero provável do nome (male/female)
    """
    key = '6b59b10fd62848298f243c274e2522a3e42ccab9c856b58ef21af6e2353a0a6a'

    # Definindo a url da requisição get à API GenerAPI.io
    url = f'https://gender-api.com/get?name={nome}&key={key}'

    # Fazendo a requisição
    resposta = requests.get(url, timeout=5)

    # Verificando o status da requisição
    if resposta.status_code != 200:
        raise ConnectionError('Erro ao conectar com a API Gender-API.com.')
    
    # Pegar os dados em formato JSON
    dados_nome = resposta.json()

    return dados_nome.get('gender')


# Testando

if __name__ == '__main__':
    print(buscar_genderize('Martha'))
