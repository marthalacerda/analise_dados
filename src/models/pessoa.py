"""
Modulo para a classe Pessoa.
Este módulo define a estrutura de uma Pessoa, com atributos provenientes de
um arquivo em /data.
Tem métodos para formatação e validação das informações recebidas.
"""

from src.models.endereco import Endereco

class Pessoa:
    """Usuario proveniente da lista de clientes
    
    Atributos:
        nome_completo (str): Nome completo da pessoa
        primeiro_nome (str): Primeiro nome da Pessoa
        segundo_nome (str): Segundo nome da Pessoa
        genero (str): Inferência do gênero da Pessoa
        email (str): Email da Pessoa
        celular (str): Celular com DDD da Pessoa
        interesse (str): Interesse de estudo da Pessoa
        cpf (str): CPF da Pessoa
        endereco (Endereco): Objeto com bairro, cidade, estado, ddd e regiao
        observacoes (list[str]): Observações sobre inconsistências nos dados
    """

    def __init__(self, pessoa_data: dict[str, str]) -> None:
        """Inicializa a instância de Pessoa.
        
        Args:
            pessoa_data (dict[str, str]): Dicionario com dados do cliente
        """
        # Dados brutos
        self.dados = pessoa_data

        self.__atribuir_nomes()
        self.genero = ''
        self.email = pessoa_data.get('Email')
        self.celular = pessoa_data.get('Celular')
        self.interesse = pessoa_data.get('Interesse')
        self.cpf = pessoa_data.get('CPF')
        self.endereco = Endereco({'bairro': '',
                                  'cidade': '',
                                  'estado': '',
                                  'ddd': '',
                                  'regiao': ''})
        self.observacoes = []


    def ler_nome(self) -> list[str]:
        """Extrai o nome completo numa lista de strings
        Formatacao com iniciais maiúsculas e preposições minúsculas.
        
        Retorna:
            Lista com o nome completo da pessoa no formato correto.
        """
        # Dado bruto de NomeCompleto
        nome_sem_tratamento = self.dados.get('NomeCompleto')

        # Nome minusculo e separado em lista
        minusculo = nome_sem_tratamento.strip().lower().split()

        # Set com preposições
        preposicoes = {'da', 'de', 'do', 'das', 'dos', 'e'}

        # formatar nome
        nome_formatado = []
        prep = False
        x = 0
        while x < len(minusculo):

            if minusculo[x] in preposicoes:
                prep = True
                x += 1
                continue

            if prep:
                nome_formatado.append(' '.join([minusculo[x-1], minusculo[x].capitalize()]))
                prep = False
                x += 1
            else:
                nome_formatado.append(minusculo[x].capitalize())
                x += 1

        return nome_formatado


    def __atribuir_nomes(self) -> None:
        """Atribui o nome completo, primeiro e segundo nome de Pessoa."""

        # Nome formatado em lista
        nome = self.ler_nome()

        # Nome completo em uma string só
        self.nome_completo = ' '.join(nome)

        # Primeiro e segundo nome em string
        self.primeiro_nome = nome[0]
        self.segundo_nome = nome[1]


    def ler_cep(self) -> str:
        """Lê o CEP de Pessoa e retorna na formatação correta com apenas números.

        Retorna:
            str: String do CEP no formato correto.
        """
        cep = self.dados.get('CEP')

        # Juntando uma lista que filtra caracteres numericos
        cep_formatado = ''.join(list(filter(lambda x: x.isdigit(), cep)))

        return cep_formatado


    def add_observacao(self, obs: str) -> None:
        """Adiciona uma observação à lista de observações da Pessoa"""
        self.observacoes.append(obs)


    # Endereço

    @property
    def endereco(self) -> Endereco:
        """Retorna objeto Endereco da Pessoa"""
        return self.__endereco

    @endereco.setter
    def endereco(self, end: Endereco) -> None:
        """Atribui objeto Endereço ao atributo endereco de Pessoa"""
        self.__endereco = end

    # Celular

    @property
    def celular(self) -> str:
        """Retorna o celular"""
        return self.__celular

    @celular.setter
    def celular(self, cel: str) -> None:
        """Atribui celular a Pessoa."""
        self.__celular = cel

    # CPF

    @property
    def cpf(self) -> str:
        """Retorna o cpf"""
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        cpf_so_numeros = ''.join(list(filter(lambda x: x.isdigit(), cpf)))
        self.__cpf = cpf_so_numeros

    # Genero

    @property
    def genero(self) -> str:
        """Retorna o genero"""
        return self.__genero

    @genero.setter
    def genero(self, genero: str) -> None:
        """Atribui genero a Pessoa"""
        self.__genero = genero



if __name__ == '__main__':
    ...
