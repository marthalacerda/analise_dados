"""Gera relatórios de análise"""

import pandas as pd



# Distribuição de gênero: % de homens e mulheres

def genero_report(data_frame: pd.DataFrame) -> None:
    """Exibe percentual de generos do DataFrame
    
    Argumentos:
        data_frame (pd.DataFrame): DataFrame que tem uma coluna genero
    """

    # Analisando os valores únicos na coluna genero e gerando o percentual (0 a 1)
    analise = data_frame['genero'].value_counts(normalize=True)

    # Dicionário para mudar o nome na impressão
    generos = {'male': 'Homens', 'female': 'Mulheres'}

    # Impressão
    print('\n📊  Distribuição de Gênero:\n')
    for item, percentual in analise.items():
        print(f'    - {generos.get(item, "Não inferido")}: {percentual:.1%}')
    print()



# Distribuição geográfica: % por região

def regiao_report(data_frame: pd.DataFrame) -> None:
    """Exibe percentual de regiões do DataFrame
    
    Argumentos:
        data_frame (pd.DataFrame): DataFrame que tem uma coluna estado
    """

    # Criando coluna de regiao a partir de função aplicada na coluna estado
    data_frame['regiao'] = data_frame['estado'].apply(buscar_regiao)

    # Analisando os valores únicos
    analise = data_frame['regiao'].value_counts(normalize=True)

    # Impressão
    print('\n🌎  Distribuição Geográfica:\n')
    for regiao, percentual in analise.items():
        print(f'    - {regiao}: {percentual:.1%}')
    print()


def buscar_regiao(uf: str) -> str:
    """Retorna a região do estado (UF)"""
    # Dicionário para definir a região a partir do estado
    regioes = {
        'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
        'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
        'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'],
        'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
        'Sul': ['PR', 'RS', 'SC']
    }

    for regiao, estados in regioes.items():
        if uf in estados:
            return regiao
    return 'Não informado'



# Qualidades dos dados: CPFs inválidos, números de telefones ausentes...

def qualidade_report(d_frame: pd.DataFrame) -> None:
    """Exibe quantidade de inconsistências nos dados

    Inconsistências analisadas:
        'Celular inválido.'
        'Celular ausente.'
        'CPF inválido.'

    Argumentos:
        data_frame (pd.DataFrame): DataFrame que tem uma coluna observacoes 
    """
    # Quantidade de cada inconsistencia
    cel_aus = d_frame['observacoes'].str.contains('Celular ausente.').sum()
    cel_inv = d_frame['observacoes'].str.contains('Celular inválido.').sum()    
    cpf_inv = d_frame['observacoes'].str.contains('CPF inválido').sum()

    # Impressão
    print('\n📋  Qualidade dos dados:\n')
    print(f'    - Celulares em branco: {cel_aus}')
    print(f'    - Celulares errados: {cel_inv}')
    print(f'    - CPFs inválidos: {cpf_inv}')

# Percentual das áreas de interesse (geral)

def interesses_report(data_frame: pd.DataFrame) -> None:
    """Exibe percentual de interesse do DataFrame
    
    Argumentos:
        data_frame (pd.DataFrame): DataFrame que tem uma coluna interesse
    """

    # Analisando valores únicos da coluna interesse
    analise = data_frame['interesse'].value_counts(normalize=True)

    # Impressão
    print('\n📚  Áreas de Interesse:\n')
    for area, percentual in analise.items():
        print(f'    - {area}: {percentual:.1%}')
    print()


# Quais áreas de intersse são mais desejadas por homens e mulheres (percentual)

def interesses_gen_report(lista_pessoas: list[dict]) -> None:
    ...




if __name__ == '__main__':

    lista = [{'nome_completo': 'André de Bifur Gomes Ribeiro', 'primeiro_nome': 'André',
            'segundo_nome': 'de Bifur', 'genero': '', 'email': 'andrebifur@testmail.org',
            'celular': '51 952127281', 'interesse': 'Desenvolvimento de Jogos Digitais',
            'cpf': '94097729828', 'bairro': 'Petrópolis', 'cidade': 'Porto Alegre', 'estado': 'RS',
            'observacoes': 'CPF inválido.'},
            {'nome_completo': 'Lucas Lima e Você', 'primeiro_nome': 'Lucas',
            'segundo_nome': 'Lima', 'genero': 'male', 'email': 'tcherreretchetche@fakemail.net',
            'celular': '31 945539436', 'interesse': 'Desenvolvimento de Jogos Digitais',
            'cpf': '97778604558', 'bairro': 'Santo Agostinho', 'cidade': 'Belo Horizonte',
            'estado': 'MG', 'observacoes': ''}]


    data_frame = pd.DataFrame(lista)
    print(type(data_frame))
    print('-' *40)
    genero_report(data_frame)
    print('-' *40)
    regiao_report(data_frame)
    print('-' *40)
    interesses_report(data_frame)
    print('-' *40)
    qualidade_report(data_frame)