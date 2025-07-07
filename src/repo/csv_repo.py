"""Leitura do arquivo csv com os dados"""

import csv
from pathlib import Path


def ler_csv(caminho_arquivo: Path) -> list[dict]:
    """Lê um arquivo csv e retorna seus dados sem tratamento
    
    Argumentos:
        caminho_arquivo: Path - caminho para o arquivo csv em ./data.
    
    Levanta:
        FileNotFoundError: Caso o arquivo não seja encontrado.
    
    Retorna:
        list[dict] - lista de registros do csv, cada um como um dicionario.
    """

    # Verificando se o caminho existe
    if not caminho_arquivo.exists():
        raise FileNotFoundError('Arquivo não encontrado.')

    # Abrindo o arquivo usando Path.open()
    with caminho_arquivo.open(mode='r', encoding='utf-8') as arquivo:

        # Transformando os dados em dicionários
        leitor = csv.DictReader(arquivo)

        return list(leitor)



# Testando a leitura e acesso ao arquivo como lista
if __name__ == '__main__':

    lista = ler_csv(Path(__file__).resolve().parent.parent.parent / "data" / "lista_clientes.csv")
    print(lista[0])
    print(lista[49])
