# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python. O sistema permite a criação de usuários, criação de contas bancárias, depósitos, saques, visualização de saldo e extrato, bem como a deleção de usuários ou contas. O projeto é modularizado para facilitar manutenção e adição de novos recursos.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

1. **Criar Usuário** - Permite a criação de um novo usuário com CPF, nome, data de nascimento, endereço, e-mail e senha.
2. **Acessar Usuário** - Permite que um usuário existente faça login, utilizando o CPF e as credenciais cadastradas.
3. **Listar Usuários** - Exibe todos os usuários cadastrados no sistema, incluindo a quantidade de contas associadas.
4. **Criar Conta** - Após criar um usuário, o sistema cria uma conta bancária associada a ele.
5. **Consultando Saldo** - Permite consultar o saldo de uma conta específica.
6. **Saque** - Permite realizar saques de uma conta bancária, considerando as limitações de saldo e número de saques permitidos.
7. **Depósito** - Permite realizar depósitos em uma conta bancária.
8. **Visualizar Extrato** - Exibe o extrato da conta bancária, com todos os registros de movimentações realizadas.
9. **Deletar Usuário ou Conta** - Permite a exclusão de um usuário ou uma conta bancária.
10. **Listar Contas** - Exibe todas as contas bancárias associadas ao usuário.

## Pré-requisitos

- Python 3.x ou superior.
- As dependências do projeto são mínimas, consistindo principalmente de funções e bibliotecas padrão do Python.

## Estrutura do Projeto

O projeto está dividido em módulos para facilitar a manutenção e extensibilidade:

- **`cliente.py`** - Define a classe `Cliente` e suas funcionalidades.
- **`conta.py`** - Define a classe `Conta` e seus métodos relacionados.
- **`menus.py`** - Contém funções responsáveis pelos menus de operação, como `menu_principal`, `menu` e `barra_carregamento`.
- **`util.py`** - Contém funções auxiliares como `input_obrigatorio`.
- **`banco.py`** - Contém o sistema bancário principal que integra todos os módulos.

## Como Executar

Para rodar o sistema, basta executar o arquivo `banco.py`:

```bash
python banco.py
