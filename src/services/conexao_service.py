"""Testa a conneção com a internet"""

import requests

def tem_conexao() -> bool:
    """Verifica se tem conexão com a internet tentando acessar o site da google
    
    Retorna:
        bool: True se a conexão funcionar, False se não
    """
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.RequestException:
        return False

if __name__ == '__main__':
    print(tem_conexao())
