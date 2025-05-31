from datetime import datetime
import os

# Função que solicita uma entrada obrigatória do usuário e converte para o tipo desejado
def input_obrigatorio(msg, tipo=str):
    # Loop infinito até o usuário inserir um valor válido
    while True:
        # Solicita a entrada do usuário e remove espaços em branco antes/depois
        entrada = input(msg).strip()

        # Verifica se a entrada está vazia
        if not entrada:
            print('Campo obrigatório, preencha corretamente.')
            continue  # Recomeça o loop caso esteja vazia

        try:
            # Tenta converter a entrada para o tipo especificado (padrão: string)
            return tipo(entrada)
        except ValueError:
            # Caso não consiga converter (ex: texto ao invés de número), exibe erro
            print(f'Valor Inválido!')


# Função que atualiza o saldo e registra o depósito no extrato da conta
def altera_valores_extrato_contas_deposito(usuario_escolhido, dict_clientes, conta_escolhida, valor_deposito, saldo):
    from conta import Conta
    with open(f"data/user/{usuario_escolhido}/contas/conta_{conta_escolhida + 1}.txt", "w") as contas:
        contas.write(
            f'Conta -> {dict_clientes[usuario_escolhido].contas[conta_escolhida].agencia} / Saldo -> R${saldo:.2f}\n')
    with open(f'data/user/{usuario_escolhido}/contas/extrato/extrato_{conta_escolhida + 1}.txt', 'a') as extrat:
        extrat.write(
            f'Depósito -> R${valor_deposito:.2f} [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]\n')
        
# Função que atualiza o saldo e registra o saque no extrato da conta
def altera_valores_extrato_contas_saque(usuario_escolhido, dict_clientes, conta_escolhida, valor_deposito, saldo):
    from conta import Conta
    with open(f"data/user/{usuario_escolhido}/contas/conta_{conta_escolhida + 1}.txt", "w") as contas:
        contas.write(
            f'Conta -> {dict_clientes[usuario_escolhido].contas[conta_escolhida].agencia} / Saldo -> R${saldo:.2f}\n')
    with open(f'data/user/{usuario_escolhido}/contas/extrato/extrato_{conta_escolhida + 1}.txt', 'a') as extrat:
        extrat.write(
            f'Saque -> R${valor_deposito:.2f} [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]\n')


os.makedirs("data/user", exist_ok=True)  # Garante que o diretório base existe
