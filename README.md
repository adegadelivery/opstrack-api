# OpsTrack API

API desenvolvida em Python utilizando Flask para gerenciamento de chamados.

## Sobre o projeto

A OpsTrack API é uma API simples desenvolvida como exercício da disciplina de Integração e Entrega Contínua.

O projeto tem como objetivo praticar:

- Desenvolvimento de uma API utilizando Flask;
- Criação de rotas HTTP;
- Uso do Git para controle de versão;
- Utilização do GitHub;
- Organização dos commits utilizando o padrão Conventional Commits;
- Separação das alterações em commits independentes.

## Tecnologias utilizadas

- Python
- Flask
- Git
- GitHub
- Visual Studio Code

## Estrutura do projeto

opstrack-api/
- hello.py
- README.md
- .gitignore

## API

A API possui quatro rotas principais:

| Método | Rota | Descrição |
|---|---|---|
| GET | / | Retorna uma mensagem inicial |
| GET | /status | Retorna o status do serviço |
| GET | /tickets | Retorna uma lista de chamados |
| GET | /sobre | Retorna informações sobre a API |

## Rota inicial

### GET /

Retorna uma mensagem inicial da API.

Resposta:

Hello World 1

## Rota de status

### GET /status

Retorna o status atual do serviço.

Resposta:

{
    "status": "online"
}

## Rota de chamados

### GET /tickets

Retorna uma lista mockada de chamados.

Resposta:

[
    {
        "id": 1,
        "titulo": "Computador não liga",
        "status": "aberto"
    },
    {
        "id": 2,
        "titulo": "Erro no sistema",
        "status": "em andamento"
    },
    {
        "id": 3,
        "titulo": "Solicitação de acesso",
        "status": "fechado"
    }
]

## Rota sobre

### GET /sobre

Retorna informações básicas sobre a API.

Resposta:

{
    "nome": "OpsTrack API",
    "versao": "1.0.0"
}

## Instalação

Para utilizar o projeto, é necessário ter o Python instalado.

Clone o repositório:

git clone https://github.com/miltonwagner/opstrack-api.git

Entre na pasta do projeto:

cd opstrack-api

Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual no Windows PowerShell:

.\venv\Scripts\Activate.ps1

Instale o Flask:

pip install flask

## Execução

Com o ambiente virtual ativado, execute:

flask --app hello run

A aplicação estará disponível em:

http://127.0.0.1:5000

## Testando as rotas

As rotas podem ser testadas pelo navegador ou utilizando o Postman.

Página inicial:

http://127.0.0.1:5000/

Status:

http://127.0.0.1:5000/status

Tickets:

http://127.0.0.1:5000/tickets

Sobre:

http://127.0.0.1:5000/sobre

## Controle de versão

O projeto utiliza Git para controle de versão e GitHub para armazenamento remoto do código.

Repositório:

https://github.com/miltonwagner/opstrack-api.git

## Conventional Commits

Os commits do projeto seguem o padrão Conventional Commits.

Cada commit representa uma única mudança lógica.

Commits utilizados no projeto:

1. feat: adiciona rota de status
2. feat: adiciona rota de tickets
3. feat: adiciona rota sobre
4. docs: atualiza documentacao das rotas

## Tipos de commit

- feat: nova funcionalidade
- fix: correção de problema
- docs: alteração na documentação
- style: alteração de formatação
- refactor: alteração na estrutura do código sem modificar a funcionalidade

## Regra de commits

Cada commit deve representar uma única mudança lógica.

Não devem ser misturadas diferentes alterações no mesmo commit.

Exemplo:

feat: adiciona rota de status

Esse commit representa somente a criação da rota /status.

Outro exemplo:

feat: adiciona rota de tickets

Esse commit representa somente a criação da rota /tickets.

A documentação deve ser atualizada separadamente:

docs: atualiza documentacao das rotas

## .gitignore

O arquivo .gitignore evita que arquivos desnecessários sejam enviados ao GitHub.

Arquivos ignorados:

- venv/
- __pycache__/
- *.pyc

## Status do projeto

Projeto desenvolvido para fins acadêmicos na disciplina de Integração e Entrega Contínua.

Status: Em desenvolvimento.



## Rodando os testes

Instale as dependências de desenvolvimento:

```
pip install -r requirements-dev.txt
```

Execute os testes:

```
pytest
```

Execute os testes com cobertura (meta mínima de 85%):

```
pytest --cov=hello --cov-report=term-missing --cov-fail-under=85
```

O relatório de cobertura gera os arquivos `.coverage` e `htmlcov/`, que já estão no `.gitignore`.
