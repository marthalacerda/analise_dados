"""
Implementa a classe Cpf
Conjunto de métodos para validação e formatação do cpf
"""
class CPF:
    """CPF formatado
    
    Parâmetros:
        cpf (str): Cadastro de Pessoa Física
    """

    def __init__(self, cpf: str) -> None:
        """Inicia classe CPF
        
        Argumentos:
            cpf (str): Cadastro de Pessoa Física (somente numeros)

        Levanta:
            ValueError: Caso o CPF seja inválido.
        """
        self.cpf = cpf

        # Verificar se tem 11 dígitos
        if len(self.cpf) != 11:
            raise ValueError('CPF inválido.')

        # Verificar se todos os digitos são iguais
        if len(set(self.cpf)) == 1:
            raise ValueError('CPF inválido.')

        if not self.__validar():
            raise ValueError('CPF inválido.')

    def __validar(self) -> bool:
        """Valida os dígitos verificadores do CPF seguindo as regras da Receita Federal
        
        Retorna:
            bool: True se o CPF é válido
        """

        # Primeiro dígito verificador
        digito1 = self.__digito_verificador(9)

        # Segundo digito verificador
        digito2 = self.__digito_verificador(10)

        return self.cpf[-2:] == f'{digito1}{digito2}'

    def __digito_verificador(self, qtd: int) -> int:
        """Define digito verificador
        
        Argumentos:
            qtd (int): Quantidade de digitos que serão multiplicados pela regra da Receita Federal
        """
        # Usando zip para formar lista de tuplas (digito, numero)
        combo = list(zip(self.cpf[:qtd], range(qtd + 1, 1, -1)))

        # Montando lista com a multiplicação de cada tupla
        combo_multi = [int(dig) * num for dig, num in combo]

        # Calculando o dígito
        soma = sum(combo_multi)
        resultado = 11 - soma % 11
        digito = resultado if resultado < 10 else 0

        return digito
