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
