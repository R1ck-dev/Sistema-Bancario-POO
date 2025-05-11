import abc
from time import sleep
from datetime import datetime

# Função que exibe o menu principal do sistema
def menu():
    tam = len('Sistema Bancário - MENU') + 4  # Define o tamanho da linha de separação
    print('-' * tam)
    print('Sistema Bancário - MENU'.center(tam))  # Centraliza o título do menu
    print('-' * tam)
    print('\n[1] Saque')
    print('[2] Depósito')
    print('[3] Visualizar Extrato')
    print('[4] Criar Usuário')
    print('[5] Criar Conta')
    print('[6] Apagar Usuário/Conta')
    print('[7] Listar Usuários')
    print('[8] Sair\n')
    print('-' * tam)


# Classe base para representar uma pessoa física
class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __repr__(self):
        return f'{self.nome} (nome) - {self.cpf} (cpf) - {self.data_nascimento} (data de nascimento) - {self.endereco} (endereco) - {self.contas} (contas)'


# Classe Cliente que herda de PessoaFisica e adiciona endereço e contas
class Cliente(PessoaFisica):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = list()  # Lista de contas associadas ao cliente

    def adicionar_conta(self, conta):
        self.contas.append(conta)


# Classe Conta representando uma conta bancária simples
class Conta:
    contador_contas = 0  # Contador total de contas criadas
    dict_extrato = dict()  # Dicionário para armazenar extratos por CPF

    def __init__(self, agencia, saldo=0.0):
        self._saldo = saldo
        self.agencia = agencia

    @staticmethod
    def criar_conta(usuario_escolhido):
        if usuario_escolhido not in dict_clientes:
            print('Usuário Inexistente')

        conta = Conta('0001')  # Cria uma nova conta com agência padrão
        dict_clientes[usuario_escolhido].adicionar_conta(conta)
        Conta.contador_contas += 1

    def __repr__(self):
        return f'Agencia -> {self.agencia} / Saldo -> R${self._saldo:.2f}'

    def saque(self, valor, usuario_escolhido):
        self.contador_saques = 5  # NOVO: contador de saques diário/resetável
        if self.contador_saques > 0 and valor <= 500 and valor <= self._saldo and valor > 0:
            self._saldo -= valor
            self.contador_saques -= 1
            if usuario_escolhido not in Conta.dict_extrato:
                Conta.dict_extrato[usuario_escolhido] = []
            # NOVO: registro do saque no extrato com data/hora
            Conta.dict_extrato[usuario_escolhido].append(
                f'Saque -> R${valor:.2f} [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]'
            )
            return self._saldo, self.contador_saques

    def deposito(self, valor, usuario_escolhido):
        if valor > 0:
            self._saldo += valor
            if usuario_escolhido not in Conta.dict_extrato:
                Conta.dict_extrato[usuario_escolhido] = []
            # NOVO: registro do depósito no extrato com data/hora
            Conta.dict_extrato[usuario_escolhido].append(
                f'Depósito -> R${valor:.2f} [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]'
            )
            return self._saldo

    @staticmethod
    def extrato(cpf):
        for item in Conta.dict_extrato[cpf]:
            print(item)


# Dicionário que armazena os clientes usando o CPF como chave
dict_clientes = dict()

# Loop principal do programa
while True:
    menu()
    operacao = str(input('Indique a operação desejada: '))

    if operacao not in '12345678':
        print('Operação não existente!')
        continue

    elif operacao == '1':
        print('Saque!')
        print('Insira qual usuário deseja acessar!')
        for chave in dict_clientes:
            print(f'{dict_clientes[chave].nome}: {chave}')
        usuario_escolhido = str(input('Indique o CPF: '))
        if len(dict_clientes[chave].contas) > 1:
            print('Indique qual conta deseja sacar!')
            for c in range(len(dict_clientes[usuario_escolhido].contas)):
                print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
            conta_escolhida = int(input())
        valor_saque = float(input('Insira o valor de saque: '))
        saldo = Conta.saque(dict_clientes[usuario_escolhido].contas[conta_escolhida], valor_saque, usuario_escolhido)
        print(f'Saldo atual = R${saldo[0]:.2f}')
        print(f'Quantidade de saques restantes = {saldo[1]}')

    elif operacao == '2':
        print('Depósito!')
        print('Insira qual usuário deseja acessar!')
        for chave in dict_clientes:
            print(f'{dict_clientes[chave].nome}: {chave}')
        usuario_escolhido = str(input('Indique o CPF: '))
        if len(dict_clientes[chave].contas) > 1:
            print('Indique qual conta deseja depositar!')
            for c in range(len(dict_clientes[usuario_escolhido].contas)):
                print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
            conta_escolhida = int(input())
        valor_deposito = float(input('Insira o valor de depósito: '))
        saldo = Conta.deposito(dict_clientes[usuario_escolhido].contas[conta_escolhida], valor_deposito, usuario_escolhido)
        print(f'Saldo -> R${saldo:.2f}')

    elif operacao == '3':
        print('Visualizar Extrato!')
        print('Deseja visualizar o extrato de qual usuário?')
        for chave in dict_clientes:
            print(f'{dict_clientes[chave].nome}: {chave}')
        usuario_escolhido = str(input('Indique o CPF: '))
        if len(dict_clientes[chave].contas) > 1:
            print('Indique qual conta deseja ver o extrato!')
            for c in range(len(dict_clientes[usuario_escolhido].contas)):
                print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
            conta_escolhida = int(input())
        Conta.extrato(usuario_escolhido)

    elif operacao == '4':
        print('Criando Usuário!')
        nome = str(input('Insira o seu nome: '))
        cpf = str(input('Insira o seu cpf: '))
        data_nascimento = str(input('Insira a sua data de nascimento: '))
        endereco = str(input('Insira o seu endereço: '))
        usuario = Cliente(cpf, nome, data_nascimento, endereco)
        dict_clientes[cpf] = usuario

    elif operacao == '5':
        print('Criando Conta!')
        print('Para qual usuário você gostaria de criar a conta.')
        for chave in dict_clientes:
            print(f'{dict_clientes[chave].nome}: {chave}')
        Conta.criar_conta(str(input('Indique o CPF: ')))

    elif operacao == '6':
        print('Deletar Usuário ou Conta')
        print('Deletar Usuário ou Conta?')
        del_escolha = str(input()).lower()
        if del_escolha == 'usuário':
            for chave in dict_clientes:
                print(f'{dict_clientes[chave].nome}: {chave}')
            usuario_escolhido = str(input('Indique o CPF: '))
            del dict_clientes[usuario_escolhido]
        elif del_escolha == 'conta':
            for chave in dict_clientes:
                print(f'{dict_clientes[chave].nome}: {chave}')
            usuario_escolhido = str(input('Indique o CPF: '))
            for c in range(0, len(dict_clientes[usuario_escolhido].contas)):
                print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
            conta_escolhida = int(input())
            del dict_clientes[usuario_escolhido].contas[conta_escolhida]
        

    elif operacao == '7':
        print('Listando Usuários!')
        for chave in dict_clientes:
            print(f'{chave} [CPF] / {dict_clientes[chave].nome} [Nome] / {len(dict_clientes[chave].contas)} [Quantidade de Contas]')

    elif operacao == '8':
        break

# Ao final, exibe o resumo dos usuários e suas contas
for chave in dict_clientes:
    print(f'{chave}: {dict_clientes[chave].nome} / {dict_clientes[chave]}')
    print(f'O usuário {dict_clientes[chave].nome}, possui {len(dict_clientes[chave].contas)} contas')
