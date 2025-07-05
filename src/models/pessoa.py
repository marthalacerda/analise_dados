"""
Modulo para a classe Pessoa.
Este módulo define a estrutura de uma Pessoa, com atributos provenientes de
um arquivo em /data.
Tem métodos para formatação e validação das informações recebidas.
"""




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
        cpf (str): CEP da Pessoa 
        bairro (str): Bairro do endereço da Pessoa
        cidade (str): Cidade do endereço da pessoa
        estado (str): Estado do endereço da Pessoa
        observacoes (list[str]): Observações sobre inconsistências nos dados
    """

    def __init__(self, pessoa_data: dict[str, str]) -> None:
        """Inicializa a instância de Pessoa.
        
        Args:
            pessoa_data (dict[str, str]): Dados da pessoa
        """


