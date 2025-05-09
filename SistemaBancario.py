import abc

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
    # print('[6] Apagar Usuário/Conta')
    # print('[7] Listar Usuários')
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
    contador_contas = 0

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
    
    def saque(self, valor):
        self.contador_saques = 5
        if self.contador_saques > 0 and valor <= 500 and valor <= self._saldo and valor > 0:
            self._saldo = self._saldo - valor
            self.contador_saques -= 1
            return self._saldo, self.contador_saques
        
    def deposito(self, valor):
        if valor > 0:
            self._saldo = self._saldo + valor
            return self._saldo

# Dicionário que armazena os clientes usando o CPF como chave
dict_clientes = dict()

# Loop principal do programa
while True:
    menu()  # Exibe o menu

    operacao = str(input('Indique a operação desejada: '))

    if operacao not in '123458':
        print('Operação não existente!')
        continue

    elif operacao == '1':
        print('Saque!')
        print('Insira qual usuário deseja acessar!')
        for chave in dict_clientes:
            print(f'{dict_clientes[chave].nome}: {chave}')
        usuario_escolhido = str(input('Indique o CPF: '))
        if len(dict_clientes[chave].contas) > 1:
            print('Indique qual conta deseja depositar!')
            for c in range(0, len(dict_clientes[usuario_escolhido].contas)):
                print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
            conta_escolhida = int(input())
        valor_saque = float(input('Insira o valor de saque: '))
        saldo = Conta.saque(dict_clientes[usuario_escolhido].contas[conta_escolhida], valor_saque)
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
            for c in range(0, len(dict_clientes[usuario_escolhido].contas)):
                print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
            conta_escolhida = int(input())
        valor_deposito = float(input('Insira o valor de depósito: '))
        saldo = Conta.deposito(dict_clientes[usuario_escolhido].contas[conta_escolhida], valor_deposito)
        print(f'Saldo -> R${saldo:.2f}')

    elif operacao == '3':
        pass  # Visualização de extrato ainda não implementada

    elif operacao == '4':
        # Criação de novo usuário
        print('Criando Usuário!')
        nome = str(input('Insira o seu nome: '))
        cpf = str(input('Insira o seu cpf: '))
        data_nascimento = str(input('Data Insira a sua data de nascimento: '))
        endereco = str(input('Insira o seu endereço: '))
        usuario = Cliente(cpf, nome, data_nascimento, endereco)
        dict_clientes[cpf] = usuario

    elif operacao == '5':
        # Criação de nova conta para um usuário existente
        print('Criando Conta!')
        print('Para qual usuário você gostaria de criar a conta.')

        for chave in dict_clientes:
            print(f'{dict_clientes[chave].nome}: {chave}')  # Exibe os usuários existentes

        Conta.criar_conta(str(input('Indique o CPF: ')))

    elif operacao == '8':
        break  # Encerra o programa

for chave in dict_clientes:
    print(f'{chave}: {dict_clientes[chave].nome} / {dict_clientes[chave]}')
    print(f'O usuário {dict_clientes[chave].nome}, possui {len(dict_clientes[chave].contas)} contas')
