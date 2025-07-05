"""Leitura do arquivo csv com os dados"""


import csv
from pathlib import Path


def ler_csv(caminho_arquivo: Path) -> list[dict]:
    """Lê um arquivo csv e retorna seus dados sem tratamento
    
    Args:
        caminho_arquivo: Path - caminho para o arquivo csv em ./data.
    
    Raises:
        FileNotFoundError: Caso o arquivo não seja encontrado.
    
    Returns:
        list[dict] - lista de registros do csv, cada um como um dicionario.
    """
    
    # Verificar se o caminho existe
    if not caminho_arquivo.exists():
        raise FileNotFoundError('Arquivo não encontrado.')

    # Abrir o arquivo usando Path.open()
    with caminho_arquivo.open(mode='r', encoding='utf-8') as arquivo:
    
        # O DictReader considera a 1a linha como cabeçalho, e depois cada linha como um dicionário.
        leitor = csv.DictReader(arquivo)
        return list(leitor)



# Testando a leitura e acesso ao arquivo como lista
if __name__ == '__main__':

    lista = ler_csv(Path(__file__).resolve().parent.parent.parent / "data" / "lista_clientes.csv")
    print(lista[0])
    print(lista[49])
