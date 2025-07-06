"""
Módulo para fazer requisição às APIs generize.io, genderapi.io e gender-api.com
Nese módulo estão implementadas funções de cada requisição
"""

import requests

def buscar_genero_generize(nome: str) -> str:
    """Faz a requisição get à API generize.io retorna os dados do nome
    
    Argumentos:
        nome (str): Primeiro nome de Pessoa

    Levanta:
        ConnectionError: Caso não seja possível a comunicação com a API.
    
    Retorna:
        str: Genero provável do nome (male/female)
    """

    # Definindo a url da requisição get à API generize.io
    url = f'https://api.genderize.io?name={nome}&country_id=BR'

    # Fazendo a requisição
    resposta = requests.get(url, timeout=5)

    # Verificando o status da requisição
    if resposta.status_code != 200:
        raise ConnectionError('Erro ao conectar com a API generize.io.')
    
    # Pegar os dados em formato JSON
    dados_nome = resposta.json()

    return dados_nome.get('gender')


# Testando

if __name__ == '__main__':
    print(buscar_genero_generize('Martha'))
