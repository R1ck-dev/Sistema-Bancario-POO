# Sistema Bancário em POO

## Descrição

Este projeto é um sistema bancário simples desenvolvido em Python, utilizando os conceitos de Programação Orientada a Objetos (POO). O sistema permite operações básicas de conta bancária como depósitos, saques, transferências e consulta de extrato.

## Funcionalidades

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

## Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/R1ck-dev/Sistema-Bancario-POO.git
```

2. Navegue até o diretório do projeto:
```bash
cd Sistema-Bancario-POO
```

3. Execute o sistema:
```bash
python main.py
```

## Estrutura do Projeto

Sistema-Bancario/
│
├── banco.py           - Lógica principal do sistema bancário (cadastro, login e operações)
├── conta.py           - Classe Conta com métodos de depósito, saque e extrato
├── cliente.py         - Classes Cliente e PessoaFisica
├── menus.py           - Funções para exibição dos menus do sistema
├── util.py            - Funções auxiliares como validação de entrada
└── README.md          - Este arquivo

## Requisitos

- Python 3.x

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
