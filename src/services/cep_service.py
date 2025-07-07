"""
Requisição à API ViaCep
Nese módulo está implementada a função para requisição.
"""

import requests
import time

def buscar_cep(cep: str) -> dict[str, str]:
    """Faz a requisição get à API ViaAPI e retorna os dados do CEP
    
    Usa cache para evitar consultas duplicadas e pausas entre requisições.

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

    # Fazendo a requisição com tempo de espera
    time.sleep(0.3)
    resposta = requests.get(url, timeout=5)

    # Verificando o status da requisição
    if resposta.status_code != 200:
        raise ConnectionError('Erro de conexão com a API ViaCEP.')
    
    # Pegar os dados em formato JSON
    dados_cep = resposta.json()

    # Verificando se veio "erro" na resposta como informado na documentação da API ViaCEP
    if 'erro' in dados_cep:
        raise ValueError('CEP não encontrado.')

    return dados_cep


# Cache simples em memória
cep_cache: dict[str, dict[str, str]] = {}

# def buscar_cep(cep: str) -> dict[str, str]:
#     """Faz a requisição à API ViaCEP e retorna os dados do CEP.
    
#     Usa cache para evitar consultas duplicadas e pausa entre requisições.

#     Argumentos:
#         cep (str): Código de Endereçamento Postal (somente números)

#     Levanta:
#         ConnectionError: Se houver falha de comunicação com a API
#         ValueError: Se o CEP não for encontrado

#     Retorna:
#         dict[str, str]: Dados completos do CEP
#     """
#     # 1. Verificar cache
#     if cep in cep_cache:
#         return cep_cache[cep]

#     # 2. Construir URL e fazer requisição
#     url = f'https://viacep.com.br/ws/{cep}/json/'

#     try:
#         resposta = requests.get(url, timeout=5)
#         resposta.raise_for_status()
#         dados_cep = resposta.json()

#         if 'erro' in dados_cep:
#             raise ValueError('CEP não encontrado.')

#         # 3. Armazenar no cache e retornar
#         cep_cache[cep] = dados_cep
#         return dados_cep

#     except requests.exceptions.RequestException:
#         raise ConnectionError('Erro de conexão com a API ViaCEP')

#     finally:
#         time.sleep(0.5)  # Pausa entre requisições

# Testando

if __name__ == '__main__':
    print(buscar_cep('51170145'))
