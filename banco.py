# Importações dos menus, utilitários e classes necessárias
from menus import menu_principal, menu, barra_carregamento
from util import input_obrigatorio
from cliente import Cliente
from conta import Conta, dict_clientes

# Função principal do sistema, gerencia a interface inicial
def sistema_principal():
    while True:
        menu_principal()  # Exibe o menu principal

        operacao = input_obrigatorio('Indique a operação desejada: ')  # Recebe a operação do usuário

        # Valida se a operação é válida
        if operacao not in '1234':
            print('Operação não existente!')
            continue

        # Cadastro de novo usuário
        elif operacao == '1':
            print('Criando Usuário!')
            nome = input_obrigatorio('Insira o seu nome: ')
            cpf = input_obrigatorio('Insira o seu CPF: ')
            
            # Verifica se o CPF já existe
            if cpf in dict_clientes:
                print('CPF já cadastrado!')
                continue

            data_nascimento = input_obrigatorio('Insira a sua data de nascimento: ')
            endereco = input_obrigatorio('Insira o seu endereço: ')
            email = input_obrigatorio('Insira o seu e-mail: ')

            # Verifica se o e-mail já está cadastrado
            email_existe = False
            for cliente in dict_clientes.values():
                if cliente._email == email:
                    email_existe = True
                    continue
            if email_existe:
                print('Email já cadastrado!')
                continue

            senha = input_obrigatorio('Insira a sua senha: ')
            
            # Cria o cliente e o adiciona ao dicionário
            usuario = Cliente(cpf, nome, data_nascimento, endereco, email, senha)
            dict_clientes[cpf] = usuario

            print('Criando primeira conta!')
            Conta.criar_conta(usuario_escolhido=cpf)
            barra_carregamento()
    
        # Acesso de usuário existente
        elif operacao == '2':
            print('Acessando Usuário!')
            usuario_escolhido = input_obrigatorio('Insira o CPF do Usuário: ')
            if usuario_escolhido in dict_clientes and Conta.valida_email_senha(usuario_escolhido):
                menu_usuario(usuario_escolhido)
            barra_carregamento()

        # Listagem de todos os usuários
        elif operacao == '3':
            print('Listando Usuários!')
            for chave in dict_clientes:
                print(f'{dict_clientes[chave].nome} [Nome] / {len(dict_clientes[chave].contas)} [Quantidade de Contas]')
            barra_carregamento()
        
        # Encerrar o sistema
        elif operacao == '4':
            barra_carregamento()
            break

# Função que mostra o menu de operações para o usuário logado
def menu_usuario(usuario_escolhido):
    while True:
        menu()  # Exibe o menu de operações do usuário
        operacao = input_obrigatorio('Indique a operação desejada: ')

        # Verifica se a operação está dentro das opções disponíveis
        if operacao not in '12345678':
            print('Operação não existente!')
            continue

        # Operação 1: Consultar saldo
        elif operacao == '1':
            print('Consultando Saldo!')
            if len(dict_clientes[usuario_escolhido].contas) > 1:
                print('Indique qual conta deseja consultar o saldo!')
                for c in range(len(dict_clientes[usuario_escolhido].contas)):
                    print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
                conta_escolhida = input_obrigatorio('', int)
            else:
                conta_escolhida = 0  
            
            if conta_escolhida < 0 or conta_escolhida >= len(dict_clientes[usuario_escolhido].contas):
                print('Conta não existente')
                continue

            conta = dict_clientes[usuario_escolhido].contas[conta_escolhida]
            print(f'R${conta.visualizar_saldo():.2f}')
            barra_carregamento()

        # Operação 2: Realizar saque
        elif operacao == '2':
            print('Saque!')
            if len(dict_clientes[usuario_escolhido].contas) > 1:
                print('Indique qual conta deseja sacar!')
                for c in range(len(dict_clientes[usuario_escolhido].contas)):
                    print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
                conta_escolhida = input_obrigatorio('', int)
            else:
                conta_escolhida = 0  

            if conta_escolhida < 0 or conta_escolhida >= len(dict_clientes[usuario_escolhido].contas):
                print('Conta não existente')
                continue

            valor_saque = input_obrigatorio('Insira o valor de saque: ', float)
            saldo = dict_clientes[usuario_escolhido].contas[conta_escolhida].saque(valor_saque, usuario_escolhido)
            print(f'Saldo atual = R${saldo[0]:.2f}')
            print(f'Quantidade de saques restantes = {saldo[1]}')
            barra_carregamento()

        # Operação 3: Realizar depósito
        elif operacao == '3':
            print('Depósito!')
            if len(dict_clientes[usuario_escolhido].contas) > 1:
                print('Indique qual conta deseja depositar!')
                for c in range(len(dict_clientes[usuario_escolhido].contas)):
                    print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
                conta_escolhida = input_obrigatorio('', int)
                if conta_escolhida < 0 or conta_escolhida >= len(dict_clientes[usuario_escolhido].contas):
                    print('Conta não existente')
                    continue
                valor_deposito = input_obrigatorio('Insira o valor de depósito: ', float)
                saldo = Conta.deposito(dict_clientes[usuario_escolhido].contas[conta_escolhida], valor_deposito, usuario_escolhido)
            else:
                valor_deposito = input_obrigatorio('Insira o valor de depósito: ', float)
                saldo = Conta.deposito(dict_clientes[usuario_escolhido].contas[0], valor_deposito, usuario_escolhido)

            print(f'Saldo -> R${saldo:.2f}')
            barra_carregamento()

        # Operação 4: Visualizar extrato
        elif operacao == '4':
            print('Visualizar Extrato!')
            if len(dict_clientes[usuario_escolhido].contas) > 1:
                print('Indique qual conta deseja ver o extrato!')
                for c in range(len(dict_clientes[usuario_escolhido].contas)):
                    print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
                conta_escolhida = input_obrigatorio('', int)
                if conta_escolhida < 0 or conta_escolhida >= len(dict_clientes[usuario_escolhido].contas):
                    print('Conta não existente')
                    continue
            Conta.extrato(usuario_escolhido)
            barra_carregamento()

        # Operação 5: Criar nova conta
        elif operacao == '5':
            print('Criando Conta!')
            Conta.criar_conta(usuario_escolhido)
            barra_carregamento()

        # Operação 6: Deletar conta ou usuário
        elif operacao == '6':
            print('Deletar Usuário ou Conta')
            print('Deletar Usuário ou Conta?')
            del_escolha = input_obrigatorio('').lower()
            if del_escolha == 'usuário':
                del dict_clientes[usuario_escolhido]
                break
            elif del_escolha == 'conta':
                for c in range(0, len(dict_clientes[usuario_escolhido].contas)):
                    print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
                conta_escolhida = input_obrigatorio('Selecione a conta à ser deletada:\n', int)
                if conta_escolhida < 0 or conta_escolhida >= len(dict_clientes[usuario_escolhido].contas):
                    print('Conta não existente')
                    continue
                del dict_clientes[usuario_escolhido].contas[conta_escolhida]
            barra_carregamento()

        # Operação 7: Listar todas as contas do usuário
        elif operacao == '7':
            print('Listando Contas!')
            for c in range(0, len(dict_clientes[usuario_escolhido].contas)):
                print(f'[{c}] - {dict_clientes[usuario_escolhido].contas[c]}')
            barra_carregamento()

        # Operação 8: Sair do menu do usuário
        elif operacao == '8':
            break
