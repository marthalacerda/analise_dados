"""
Módulo da classe PessoaController
Esta classe tem todos os métodos necessários para o fluxo de criação do objeto Pessoa

Fluxo:
1. Instanciar Pessoa com dados brutos do Banco de Dados
2. Instanciar Endereco através do CEP
3. Formatar celular baseando no ddd
4. Validar CPF
5. Inferir o gênero
6. Retornar Pessoa com dados completos
"""

# import sys
# import os

# # Apagar depois
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pathlib import Path
from src.repo.csv_repo import ler_csv
from src.models.pessoa import Pessoa
from src.models.endereco import Endereco
from src.services import cep_service, gender_service
from src.models.cpf import CPF

class PessoaController:
    """Classe com métodos para a montagem de objeto Pessoa
    Faz o controle do fluxo de criação, chamando todos os métodos
    para obter as informações necessárias para completar o objeto Pessoa.
    
    Parâmetros:
        opcao_genero (str): Escolha do usuário para a API que vai inferir o gênero de Pessa."""

    def __init__(self, opcao_genero):
        """Inicia o Controller
        
        Argumentos:
            opcao_genero (str): Escolha do usuário
        """
        self.opcao_genero = opcao_genero


    # Método principal de criação de Pessoa
    def construir_pessoa(self, dados_pessoa: dict) -> Pessoa:
        """Função para construir uma instância de Pessoa.
        
        Argumentos:
            dados_pessoa: Dicionário com as informações do cliente no banco de dados
        
        Retorna:
            Pessoa: Instância de Pessoa
        """

        # Criando Pessoa (nomes formatados)
        pessoa = Pessoa(dados_pessoa)

        # Criando e atribuindo Endereco
        try:
            pessoa.endereco = self.__criar_endereco(pessoa)
        except (ValueError, ConnectionError) as e:
            print(e)

        # Verificando e formatando o celular
        try:
            pessoa.celular = self.__formatar_celular(pessoa)
        except ValueError as e:
            pessoa.add_observacao(str(e))

        # Validando o CPF
        try:
            self.__validar_cpf(pessoa)
        except ValueError as e:
            pessoa.add_observacao(str(e))

        # Inferindo gênero baseado na opção do usuário
        try:
            pessoa.genero = self.__buscar_genero(pessoa, self.opcao_genero)
        except ConnectionError as e:
            print(e)

        return pessoa


    # Métodos auxiliares

    def __validar_cpf(self, pessoa: Pessoa) -> None:
        """Instancia CPF com o cpf da Pessoa e faz a validação
        
        Argumentos:
            pessoa (Pessoa): Objeto Pessoa que terá o cpf validado
        
        Levanta:
            ValueError: Caso o CPF seja inválido.
        """
        cpf = pessoa.cpf
        CPF(cpf)


    def __criar_endereco(self, pessoa: Pessoa) -> Endereco:
        """Função que busca as informações do cep via API e cria endereço.
        
        Argumentos:
            pessoa (Pessoa): Objeto Pessoa que vai fornecer o cep

        Levanta:
            ValueError: CEP não encontrado
            ConnectionError: Erro na conexão com a API

        Retorna:
            Endereco: Instância da classe Endereco
        """
        cep = pessoa.ler_cep()

        # Buscar os dados do CEP
        dados_cep = cep_service.buscar_cep(cep)

        # Retornar instancia de endereço
        return Endereco(dados_cep)


    def __formatar_celular(self, pessoa: Pessoa) -> str:
        """Ajeita o número do celular na formação dos requisitos.
        'DD 9XXXXXXXX'
        
        Argumentos:
            pessoa (Pessoa): Objeto Pessoa que sofrerá a formatação do celular
        
        Retorna:
            str: Celular formatado
        """
        # Filtrando o celular para ficar apenas com dígitos numéricos
        cel = ''.join(filter(lambda x: x.isdigit(), pessoa.celular))

        # Verificando campo vazio e celular inválido
        if not cel:
            raise ValueError('Celular inexistente.')

        if 8 > len(cel) > 0 or len(cel) > 11:
            raise ValueError('Celular inválido.')

        if len(cel) > 8 and cel[-9] != '9':
            raise ValueError('Celular inválido.')

        # Formatando o celular
        if len(cel) == 8:
            cel = f'{pessoa.endereco.ddd} 9{cel}'
        elif len(cel) == 9:
            cel = f'{pessoa.endereco.ddd} {cel}'
        elif len(cel) == 10:
            cel = f'{cel[:2]} 9{cel[2:]}'
        elif len(cel) == 11:
            cel = f'{cel[:2]} {cel[2:]}'

        return cel


    def __buscar_genero(self, pessoa: Pessoa, opcao: str) -> str:
        """Acessa API para inferir o gênero de Pessoa
        '1' chama genderize.io
        '2' chama genderapi.io
        '3' chama gender-api.com

        Argumentos:
            pessoa (Pessoa): Objeto Pessoa que vai fornecer o nome
            opcao (str): Escolha do usuário

        Levanta:
            ConnentionError: Caso tenha erro na conexão com a API 
            
        Retorna:
            str: Genero da pessoa (male/female)
        """
        nome = pessoa.primeiro_nome

        # Chamar a função da API escolhida pelo usuário
        match opcao:
            case '1':
                return gender_service.buscar_genderize(nome)

            case '2':
                return gender_service.buscar_genderapi(nome)

            case '3':
                return gender_service.buscar_genderapicom(nome)

            case _:
                return ''


    def to_dict(self, pessoa: Pessoa) -> dict:
        """Transforma estrutura de Pessoa em dicionario
        Chama o método to_dict() de Pessoa
        
        Argumentos:
            pessoa (Pessoa): Objeto Pessoa que será estruturada
        
        Retorna:
            dict: Estrutura de Pessoa para salvar em arquivo
        """
        return pessoa.to_dict()







if __name__ == '__main__':


    # Ler o arquivo CSV e colocar dados numa lista de dicionarios
    lista_clientes = ler_csv(Path(__file__).resolve().parent.parent.parent\
                            /"data"/"lista_clientes.csv")

    # Separando um item qualquer da lista
    dados = lista_clientes[42]

    # Classe controller
    control = PessoaController('')

    # construir pessoa
    pessoa1 = control.construir_pessoa(dados)

    print(pessoa1.__dict__)
    print()
    print(pessoa1.to_dict())




