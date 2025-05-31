import os
from datetime import datetime

# Classe base que representa uma pessoa física no sistema
class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf  # CPF da pessoa
        self.nome = nome  # Nome completo
        self.data_nascimento = data_nascimento  # Data de nascimento

    # Método especial para representar a pessoa como string 
    def __repr__(self):
        # Retorna uma string representando os principais dados da pessoa
        return f'{self.nome} (nome) - {self.cpf} (cpf) - {self.data_nascimento} (data de nascimento) - {self.endereco} (endereco) - {self.contas} (contas)'
    
    def criar_usuario_bancoDados(self, usuario_escolhido, dict_clientes):
        from conta import Conta  # Importa aqui para evitar import circular
        # Cria o diretório para armazenar as contas do usuário, se não existir
        os.makedirs(f"data/user/{usuario_escolhido}/contas", exist_ok=True)
        # Cria ou atualiza o arquivo com os dados pessoais do usuário
        with open(f"data/user/{usuario_escolhido}/personalData.txt", "a") as personalData:
            personalData.write(
                f'Nome -> {dict_clientes[usuario_escolhido].nome}\n'
                f'CPF -> {dict_clientes[usuario_escolhido].cpf}\n'
                f'Email -> {dict_clientes[usuario_escolhido]._email}\n'
                f'Senha -> {dict_clientes[usuario_escolhido]._senha}\n'
            )
            return Conta

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
        self.contas.append(conta)  # Adiciona a conta à lista de contas do cliente
