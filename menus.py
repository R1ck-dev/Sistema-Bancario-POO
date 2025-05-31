# Importa o módulo time para usar o sleep() e simular carregamento
import time

# Função para exibir o menu principal do sistema
def menu_principal():
    # Define o título do menu
    titulo = ' Sistema Bancário - MENU INICIAL '
    # Calcula o tamanho do título para ajustar a moldura
    tam = len(titulo)
    
    # Imprime a moldura superior com base no tamanho do título
    print('\n' + '╔' + '═' * tam + '╗')
    print('║' + titulo + '║')  # Linha com o título centralizado
    print('╚' + '═' * tam + '╝\n')  # Moldura inferior

    # Opções do menu principal com emojis para representar ações
    print('  [1] 🧾 Criar Usuário')
    print('  [2] 🔑 Acessar Usuário')
    print('  [3] 📄 Listar Usuários')
    print('  [4] ❌ Sair\n')

    # Linha decorativa inferior
    print('═' * (tam + 2))

# Função para exibir o menu de operações do usuário
def menu():
    # Define o título do menu
    titulo = ' Sistema Bancário - MENU '
    # Calcula o tamanho do título para ajustar a moldura
    tam = len(titulo)
    
    # Imprime a moldura com o título
    print('\n' + '╔' + '═' * tam + '╗')
    print('║' + titulo + '║')  # Linha com o título
    print('╚' + '═' * tam + '╝\n')  # Moldura inferior

    # Opções disponíveis para o usuário após logar
    print('  [1] 💰 Consultar Saldo')
    print('  [2] 💸 Saque')
    print('  [3] 🏦 Depósito')
    print('  [4] 📊 Visualizar Extrato')
    print('  [5] ➕ Criar Conta')
    print('  [6] ❌ Apagar Usuário/Conta')
    print('  [7] 📋 Listar Contas')
    print('  [8] 🔙 Voltar\n')

    # Linha decorativa inferior
    print('═' * (tam + 2))

# Função que simula uma barra de carregamento
def barra_carregamento(texto="⏳ Aguardando", duracao=2):
    # Exibe o texto inicial (ex: "⏳ Aguardando")
    print(f"\n{texto}", end=' ')

    # Loop que imprime blocos █ simulando progresso
    for _ in range(duracao * 4):  # Multiplicado por 4 para ter 0.25s * 4 = 1s por unidade de tempo
        print('█', end='', flush=True)  # flush=True força a saída imediata do caractere
        time.sleep(0.25)  # Pausa de 0.25 segundos entre cada bloco

    # Pula linha após terminar o carregamento
    print('\n')
