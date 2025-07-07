"""Funções para salvar arquivos JSON"""

import json
import os

def salvar_json(dados: list[dict], caminho: str = "output/users.json") -> None:
    """Salva os dados da lista em um arquivo JSON
    
    Argumentos:
        dados (list): Lista de dicionarios
        caminho (str): Caminho onde será salvo o arquivo
    """

    # Criando diretório caso não exista
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    # Escrevendo o arquivo
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump({"users": dados}, f, ensure_ascii=False, indent=2)
