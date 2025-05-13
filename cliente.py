# Classe base que representa uma pessoa física no sistema
class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf  # CPF da pessoa
        self.nome = nome  # Nome completo
        self.data_nascimento = data_nascimento  # Data de nascimento

    # Método especial para representar a pessoa como string 
    def __repr__(self):
        return f'{self.nome} (nome) - {self.cpf} (cpf) - {self.data_nascimento} (data de nascimento) - {self.endereco} (endereco) - {self.contas} (contas)'

# Classe Cliente que herda de PessoaFisica
class Cliente(PessoaFisica):
    def __init__(self, cpf, nome, data_nascimento, endereco, email, senha):
        # Chama o construtor da classe base para inicializar cpf, nome e data de nascimento
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco  # Endereço do cliente
        self._email = email  # Email (protegido)
        self._senha = senha  # Senha (protegida)
        self.contas = list()  # Lista para armazenar as contas associadas ao cliente

    # Método para adicionar uma nova conta à lista de contas do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)
