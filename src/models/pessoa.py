"""
Modulo para a classe Pessoa.
Este módulo define a estrutura de uma Pessoa, com atributos provenientes de
um arquivo em /data.
Tem métodos para formatação e validação das informações recebidas.
"""




from pathlib import Path


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
        # Dados brutos
        self.dados = pessoa_data

        # Dados que não precisam ser tratados
        self.email = pessoa_data.get('Email')
        self.interesse = pessoa_data.get('Interesse')
        self.observacoes = []

        # Dados que precisam tratar formatação

        # self.nome_completo - será atribuído dentro da função
        # self.primeiro_nome - será atribuído dentro da função
        # self.segundo_nome - será atribuído dentro da função
        self.__atribuir_nomes()

        # self.celular
        # self.cpf

        # Dados acessados via API
        # self.genero
        # self.cpf
        # self.bairro
        # self.cidade
        # self.estado

        

        


    
    def ler_nome(self) -> list[str]:
        """Extrai o nome completo numa lista de strings
        Formatacao com iniciais maiúsculas e preposições minúsculas.
        
        Returns:
            Lista com o nome completo da pessoa no formato correto"""
        
        nome_sem_tratamento = self.dados.get('NomeCompleto')   # nome pega o dado bruto de NomeCompleto

        # nome minusculo e separado em lista
        nome_minusculo = nome_sem_tratamento.strip().lower().split()

        # set com preposições
        preposicoes = {'da', 'de', 'do', 'das', 'dos', 'e'}

        # formatar nome
        # nome_formatado = []
        # for n in nome_minusculo:
        #     if n in preposicoes:
        #         nome_formatado.append(n)
        #     else:
        #         nome_formatado.append(n.capitalize())

        nome_formatado = []
        prep = False
        x = 0
        while x < len(nome_minusculo):
            
            if nome_minusculo[x] in preposicoes:
                prep = True
                x += 1
                continue
            
            if prep:
                nome_formatado.append(' '.join([nome_minusculo[x-1], nome_minusculo[x].capitalize()]))
                prep = False
                x += 1
            else:
                nome_formatado.append(nome_minusculo[x].capitalize())
                x += 1

        return nome_formatado
    

    def __atribuir_nomes(self) -> None:
        """Atribui o nome completo, primeiro e segundo nome de Pessoa."""
        
        # Nome formatado em lista
        nome = self.ler_nome()

        # Nome completo em uma string só
        self.nome_completo = ' '.join(nome)

        # Primeiro nome em string
        self.primeiro_nome = nome[0]

        # Segundo nome (se for preposição incluir o "3o nome")
        self.segundo_nome = nome[1]




        
       





if __name__ == '__main__':
    ...
    
