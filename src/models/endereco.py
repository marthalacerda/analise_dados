"""
Módulo para a classe Endereco.
A estrutura de endereço será incorporado à classe Pessoa.
Atribui somente os dados requisitados pelo sistema.
A classe é construída a partir da seguinte estrutura de dados:
{
'cep': ''
'logradouro': ''
'complemento': ''
'unidade': ''
'bairro': ''
'localidade': ''
'uf': ''
'estado': ''
'regiao': ''
'ibge': ''
'gia': ''
'ddd': ''
'siafi': ''
}
"""

class Endereco:
    """Representação de Endereço a partir de um conjunto de dados.
    
    Atributos:
    bairro (str): Bairro do endereço
    cidade (str): Cidade do endereço
    estado (str): Estado do endereço
    ddd (str): Código de área do endereço
    regiao (str): Região do endereço
    """

    def __init__(self, dados: dict[str, str]) -> None:
        '''Inicializa a classe Endereço
        
        Argumentos:
            dados (dict[str, str]): Dados do CEP
        '''
        self.bairro = dados.get('bairro', '')
        self.cidade = dados.get('localidade', '')
        self.estado = dados.get('uf', '')
        self.ddd = dados.get('ddd', '')
        self.regiao = dados.get('regiao', '')

    # Encapsulando
    @property
    def bairro(self) -> str:
        """Retorna o bairro"""
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro_novo: str) -> None:
        """Atribui bairro"""
        self.__bairro = bairro_novo
    
    @property
    def cidade(self) -> str:
        """Retorna o cidade"""
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade_nova: str) -> None:
        """Atribui cidade"""
        self.__cidade = cidade_nova

    @property
    def estado(self) -> str:
        """Retorna o estado"""
        return self.__estado
    
    @estado.setter
    def estado(self, estado_novo: str) -> None:
        """Atribui estado"""
        self.__estado = estado_novo

    @property
    def ddd(self) -> str:
        """Retorna o ddd"""
        return self.__ddd
    
    @ddd.setter
    def ddd(self, ddd_novo: str) -> None:
        """Atribui ddd"""
        self.__ddd = ddd_novo

    @property
    def regiao(self) -> str:
        """Retorna o regiao"""
        return self.__regiao
    
    @regiao.setter
    def regiao(self, regiao_nova: str) -> None:
        """Atribui regiao"""
        self.__regiao = regiao_nova
