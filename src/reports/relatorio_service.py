"""Gera relatórios de análise"""

import pandas as pd



# Distribuição de gênero: % de homens e mulheres

def genero_report(df: pd.DataFrame) -> None:
    """Exibe percentual de generos do DataFrame
    
    Argumentos:
        df (pd.DataFrame): DataFrame que tem uma coluna genero
    """

    df['gen_pt'] = df['genero'].apply(trocar_genero)
    analise = df['gen_pt'].value_counts(normalize=True)

    # Impressão
    print('\n📊  Distribuição de Gênero:\n')
    for genero, percentual in analise.items():
        print(f'    | {percentual:>7.1%} | {genero}')
    print()

def trocar_genero(gender: str) -> str:
    """Substitui o genero em inglês por português"""

    generos = {'male': 'Homens', 'female': 'Mulheres'}
    return generos.get(gender, 'Sem gênero')


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
        print(f'    | {percentual:>7.1%} | {regiao}')
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
        'Nome em branco.'
        'Nome incompleto.'
        'Celular inválido.'
        'Celular ausente.'
        'CPF inválido.'

    Argumentos:
        data_frame (pd.DataFrame): DataFrame que tem uma coluna observacoes 
    """
    # Quantidade de cada inconsistencia
    nom_bra = d_frame['observacoes'].str.contains('Nome em branco.').sum()
    cep_err = d_frame['observacoes'].str.contains('CEP não encontrado.').sum()
    nom_inc = d_frame['observacoes'].str.contains('Nome incompleto.').sum()
    cel_aus = d_frame['observacoes'].str.contains('Celular ausente.').sum()
    cel_inv = d_frame['observacoes'].str.contains('Celular inválido.').sum()
    cel_ddd = d_frame['observacoes'].str.contains('Celular sem DDD.').sum()
    cpf_inv = d_frame['observacoes'].str.contains('CPF inválido.').sum()

    # Impressão
    print('\n📋  Qualidade dos dados:\n')
    print(f'    | {nom_bra + nom_inc:^7} | Nomes em branco/incompletos')
    print(f'    | {cep_err:^7} | CEPs não encontrados')
    print(f'    | {cel_aus:^7} | Celulares em branco')
    print(f'    | {cel_inv:^7} | Celulares errados')
    print(f'    | {cel_ddd:^7} | Celulares sem DDD')
    print(f'    | {cpf_inv:^7} | CPFs inválidos')
    print()


# Percentual das áreas de interesse (geral)

def interesses_report(data_frame: pd.DataFrame) -> None:
    """Exibe percentual de interesse do DataFrame
    
    Argumentos:
        data_frame (pd.DataFrame): DataFrame que tem uma coluna interesse
    """

    # Analisando valores únicos da coluna interesse
    analise = data_frame['interesse'].value_counts(normalize=True)

    # Impressão
    print('\n🎯  Áreas de Interesse:\n')
    for area, percentual in analise.items():
        print(f'    | {percentual:>7.1%} | {area}')
    print()


# Quais áreas de intersse são mais desejadas por homens e mulheres (percentual)

# def interesses_gen_report(df: pd.DataFrame) -> None:
#     """Exibe percentual de área de interesse por gênero
    
#     Argumentos:
#         df (pd.DataFrame): DataFrame que tem as colunas genero e interesse
#     """
#     df['gen_pt'] = df['genero'].apply(trocar_genero)
#     analise = df.groupby('gen_pt')['interesse'].value_counts(normalize=True)
    
#     # Impressão
#     print('\n📚  Interesses por gênero:\n')
#     for (gen_pt, interesse), percentual in analise.items():
#         print(f'    | {percentual:>7.1%} | {gen_pt:^10} | {interesse}')
#     print()

def interesses_gen_report(df: pd.DataFrame) -> None:
    """Exibe percentual de área de interesse por gênero
    
    Argumentos:
        df (pd.DataFrame): DataFrame que tem as colunas genero e interesse
    """
    df['gen_pt'] = df['genero'].apply(trocar_genero)
    # analise = df.groupby('gen_pt')['interesse'].value_counts(normalize=True)
    
    # Impressão
    print('\n📚  Top 3 interesses por gênero:\n')
    for genero, grupo in df.groupby('gen_pt'):
        print(f'- {genero}:')
        interesse_pct = grupo['interesse'].value_counts(normalize=True).head(3)

        for interesse, percentual in interesse_pct.items():
            print(f'    | {percentual:>7.1%} | {interesse}')
    
    # for (gen_pt, interesse), percentual in analise.items():
    #     print(f'    | {percentual:>7.1%} | {gen_pt:^10} | {interesse}')
    print()



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
    print('-' *40)
    interesses_gen_report(data_frame)

    