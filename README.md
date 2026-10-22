# 💰 Sistema Bancário com Python e SQLite

Um projeto de sistema bancário desenvolvido em **Python**, utilizando **SQLite3** para armazenar e gerenciar os dados dos usuários. O sistema funciona diretamente no terminal e permite realizar operações básicas de gerenciamento de saldos.

## 📋 Funcionalidades

- **Cadastrar usuário:** registra um usuário com nome e saldo inicial.
- **Sacar:** realiza a retirada de um valor do saldo cadastrado.
- **Depositar:** adiciona um valor ao saldo do usuário.
- **Consultar saldo:** exibe o saldo de um usuário cadastrado.
- **Excluir registros:** permite remover um usuário específico ou apagar todos os registros da tabela.
- **Banco de dados persistente:** armazena as informações em um banco SQLite local.
- **Menu interativo:** oferece navegação por opções numéricas no terminal.
- **Mensagens coloridas:** utiliza códigos ANSI para diferenciar mensagens de sucesso, erro e alerta.

## 🛠️ Tecnologias utilizadas

- **Python 3.12 ou superior:** linguagem utilizada no desenvolvimento.
- **SQLite3:** banco de dados relacional integrado ao Python.
- **Pathlib:** gerenciamento do caminho do arquivo do banco de dados.
- **Terminal:** interface de interação com o usuário.

Não é necessário instalar bibliotecas externas para utilizar as funcionalidades básicas do projeto.

## 📁 Estrutura do projeto

```text
projeto_sqlite3/
├── main.py             # Arquivo principal e menu do sistema
├── funcoes.py          # Cadastro e operações bancárias
├── ler_num.py          # Leitura e validação de valores numéricos
├── sistema.bancario    # Arquivo do banco de dados SQLite
└── README.md           # Documentação do projeto
```

O arquivo `sistema.bancario` é criado automaticamente pelo programa caso ainda não exista.

## 🚀 Como executar

### 1. Pré-requisitos

Instale o Python 3.12 ou superior e verifique se ele está disponível no terminal:

```bash
python --version
```

### 2. Clone o repositório

```bash
git clone https://github.com/luigigianellini-ship-it/projeto_sqlite3.git
```

### 3. Entre na pasta do projeto

```bash
cd projeto_sqlite3
```

### 4. Execute o programa

```bash
python main.py
```

No Windows, caso necessário, você também pode utilizar:

```bash
py main.py
```

## 🖥️ Como utilizar

Ao iniciar o programa, será apresentado um menu com as seguintes opções:

| Opção | Operação |
|---|---|
| 1 | Cadastrar usuário |
| 2 | Sacar |
| 3 | Depositar |
| 4 | Exibir saldo |
| 5 | Apagar registros |
| 6 | Sair |

Selecione a opção desejada e siga as instruções exibidas no terminal.

## 🗄️ Banco de dados

O projeto utiliza o SQLite3 para armazenar os dados localmente. A tabela `sistema_bancario` possui os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER | Identificador único do registro |
| `nome` | TEXT | Nome do usuário |
| `saldo` | REAL | Saldo armazenado |

As operações de cadastro, depósito, saque e exclusão atualizam o banco de dados, permitindo que os registros permaneçam disponíveis após o encerramento do programa.

## 🎯 Objetivo do projeto

O objetivo é praticar conceitos fundamentais de programação em Python, incluindo:

- Modularização e reutilização de funções.
- Estruturas condicionais e de repetição.
- Entrada e validação de dados.
- Operações CRUD (criação, consulta, atualização e exclusão).
- Integração com banco de dados SQLite.
- Execução de comandos SQL e persistência de informações.

## ⚠️ Observação

Este projeto tem finalidade educacional e demonstra operações bancárias básicas. Ele não deve ser utilizado para administrar dinheiro real ou como um sistema bancário de produção.

## 👨‍💻 Autor

Desenvolvido por [luigigianellini-ship-it](https://github.com/luigigianellini-ship-it).

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!
