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

    # Representação textual do cliente (comentada)
    # def __repr__(self):
    #     return f'{self.nome} (nome), {self.data_nascimento} (data de nascimento), {self.endereco} (endereço)'


# Classe Conta representando uma conta bancária simples
class Conta:
    def __init__(self, agencia, saldo=0.0):
        self._saldo = saldo
        self.agencia = agencia

    def __repr__(self):
        return f'Agencia -> {self.agencia} / Saldo -> R${self._saldo:.2f}'


# Dicionário que armazena os clientes usando o CPF como chave
dict_clientes = dict()

# Lista geral de contas (não utilizada neste trecho do código)
list_contas = list()


# Loop principal do programa
while True:
    menu()  # Exibe o menu

    operacao = str(input('Indique a operação desejada: '))

    if operacao not in '123458':
        print('Operação não existente!')
        continue

    elif operacao == '1':
        pass  # Operação de saque ainda não implementada

    elif operacao == '2':
        pass  # Operação de depósito ainda não implementada

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
        dict_clientes[cpf] = usuario  # Armazena o cliente no dicionário

    elif operacao == '5':
        # Criação de nova conta para um usuário existente
        print('Criando Conta!')
        print('Para qual usuário você gostaria de criar a conta.')

        for chave in dict_clientes:
            print(f'{dict_clientes[chave].nome}: {chave}')  # Exibe os usuários existentes

        usuario_escolhido = str(input('Indique o CPF: '))

        if usuario_escolhido not in dict_clientes:
            print('Usuário Inexistente')

        conta = Conta('0001')  # Cria uma nova conta com agência padrão

        dict_clientes[usuario_escolhido].adicionar_conta(conta)

    elif operacao == '8':
        break  # Encerra o programa


# Exibe todos os clientes e suas informações
# for chave in dict_clientes:
#     print(f'{chave}: {dict_clientes[chave].nome} / {dict_clientes[chave].data_nascimento} / {dict_clientes[chave].endereco}')

for chave in dict_clientes:
    print(f'{chave}: {dict_clientes[chave].nome} / {dict_clientes[chave]}')
