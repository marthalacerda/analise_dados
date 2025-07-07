"""
Requisição à API ViaCep
Nese módulo está implementada a função para requisição.
"""

import requests

def buscar_cep(cep: str) -> dict[str, str]:
    """Faz a requisição get à API ViaAPI e retorna os dados do CEP
    
    Argumentos:
        cep (str): Código de Endereçamento Postal

    Levanta:
        ConnectionError: Caso não seja possível a comunicação com a API.
        ValueError: Caso o CEP não seja encontrado.
    
    Retorna:
        dict[str, str]: JSON com dados do CEP
    """

    # Definindo a url da requisição get à API ViaCEP
    url = f'https://viacep.com.br/ws/{cep}/json/'

    # Fazendo a requisição
    resposta = requests.get(url, timeout=5)

    # Verificando o status da requisição
    if resposta.status_code != 200:
        raise ConnectionError('Erro ao conectar com a API ViaCEP.')
    
    # Pegar os dados em formato JSON
    dados_cep = resposta.json()

    # Verificando se veio "erro" na resposta como informado na documentação da API ViaCEP
    if 'erro' in dados_cep:
        raise ValueError('CEP não encontrado.')

    return dados_cep


# Testando

if __name__ == '__main__':
    print(buscar_cep('12345678'))
