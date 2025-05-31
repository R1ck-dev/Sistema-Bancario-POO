# Importa o módulo datetime para manipular datas e horários
from datetime import datetime

# Importa a classe Cliente de outro módulo
from cliente import Cliente

# Importa o módulo os para manipular arquivos e diretórios do sistema operacional
import os

# Define a classe Conta, responsável pelas funcionalidades bancárias
class Conta:
    # Variável de classe para contar o número total de contas criadas
    contador_contas = 0

    # Dicionário de classe que armazena os extratos por CPF de usuário
    dict_extrato = dict()

    # Método construtor da classe Conta
    def __init__(self, agencia, saldo=0.0):
        self._saldo = saldo  # Saldo da conta (protegido)
        self.agencia = agencia  # Número da agência
        self.contador_saques = 5  # Limite diário de saques
        self.ultimo_saque = datetime.now().strftime('%d/%m/%Y')  # Data do último saque
        self.file = None  # Inicializa o arquivo como None

    # Método estático que cria uma nova conta para um usuário
    @staticmethod
    def criar_conta(usuario_escolhido):
        # Verifica se o usuário existe no dicionário de clientes
        if usuario_escolhido not in dict_clientes:
            print('Usuário Inexistente')
            return
        # Conta quantas contas o usuário já tem
        num_contas_usuario = len(dict_clientes[usuario_escolhido].contas) + 1
        # Cria uma nova conta com agência padrão '0001'
        conta = Conta('0001')
        # Associa a nova conta ao usuário escolhido
        dict_clientes[usuario_escolhido].adicionar_conta(conta)
        Conta.contador_contas += 1
        # Cria arquivos usando o contador do usuário
        with open(f'data/user/{usuario_escolhido}/contas/conta_{num_contas_usuario}.txt', 'a') as file:
            file.write(f'Conta [{num_contas_usuario}] -> {conta.agencia} / Saldo -> R${conta._saldo:.2f}\n')
        os.makedirs(f"data/user/{usuario_escolhido}/contas/extrato", exist_ok=True)
        with open(f'data/user/{usuario_escolhido}/contas/extrato/extrato_{num_contas_usuario}.txt', 'a') as file:
            file.write(f'Conta {num_contas_usuario}\n')

    # Método estático para validar email e senha de um usuário específico
    def valida_email_senha(usuario_escolhido):
        print('Insira o email e senha do usuário escolhido: ')
        email_insira = str(input('Email: '))
        senha_insira = str(input('Senha: '))
        # Verifica se o email e senha coincidem com os dados do usuário
        if email_insira == dict_clientes[usuario_escolhido]._email:
            if senha_insira == dict_clientes[usuario_escolhido]._senha:
                return True
            else:
                print('Senha Errada!')
        else:
            print('Email Errado!')

    # Representação textual da conta (usada para print ou debug)
    def __repr__(self):
        return f'Agencia -> {self.agencia} / Saldo -> R${self._saldo:.2f}'

    # Método que realiza o saque, verificando limites e atualizando extrato
    def saque(self, valor, usuario_escolhido):
        hoje = datetime.now().strftime('%d/%m/%Y')
        # Se o saque for em um novo dia, reseta o contador de saques
        if hoje != self.ultimo_saque:
            self.contador_saques = 5
            self.ultimo_saque = hoje
        # Verifica se o saque está dentro das condições permitidas
        if self.contador_saques > 0 and valor <= 500 and valor <= self._saldo and valor > 0:
            self._saldo -= valor  # Deduz o valor do saldo
            self.contador_saques -= 1  # Reduz o número de saques disponíveis
            # Inicializa a lista de extrato do usuário, se necessário
            if usuario_escolhido not in Conta.dict_extrato:
                Conta.dict_extrato[usuario_escolhido] = []
            # Registra o saque no extrato
            Conta.dict_extrato[usuario_escolhido].append(
                f'Saque -> R${valor:.2f} [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]'
            )
            return self._saldo, self.contador_saques
        else:
            print('Saque não permitido. Verifique valor ou limite diário.')
            return self._saldo, self.contador_saques

    # Método que realiza o depósito e atualiza o extrato
    def deposito(self, valor, usuario_escolhido):
        if valor > 0:
            self._saldo += valor  # Adiciona o valor ao saldo
            # Inicializa a lista de extrato do usuário, se necessário
            if usuario_escolhido not in Conta.dict_extrato:
                Conta.dict_extrato[usuario_escolhido] = []
            # Registra o depósito no extrato
            Conta.dict_extrato[usuario_escolhido].append(
                f'Depósito -> R${valor:.2f} [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]'
            )
            return self._saldo

    # Método estático que exibe o extrato de transações de um usuário
    @staticmethod
    def extrato(usuario_escolhido):
        if usuario_escolhido in Conta.dict_extrato and Conta.dict_extrato[usuario_escolhido]:
            for item in Conta.dict_extrato[usuario_escolhido]:
                print(item)
        else:
            print('Nenhuma transação registrada para este CPF.')

    # Método que retorna o saldo atual da conta
    def visualizar_saldo(self):
        # Retorna o saldo atual da conta
        return self._saldo

# Dicionário global que armazena todos os clientes cadastrados no sistema
dict_clientes = dict()
