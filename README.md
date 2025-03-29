# TODO List - Gerenciador de projetos e tarefas

## Sobre o projeto

Este será um sistema Web desenvolvido em Django para gerenciamento de projetos e tarefas, sejam pessoais ou em grupo. A aplicação permitirá:

-   Cadastro de projetos e suas respectivas tarefas
-   Gerenciamento de usuários/pessoas envolvidas nos projetos
- Espaço para anotações relacionadas a cada projeto ou tarefa

Os projetos e notas poderão ou não ser publicados para que os demais usuários possam acessar, para que haja melhor separação entre projetos pessoais ou em grupo.
Pretendo també, criar restrições para que apenas os usuários autorizados possam acessar determinados projetos e notas

## Tecnologias utilizadas

- Python
- Django
- Banco de dados: PostgreSQL
- Frontend: Django templates, HTML, CSS e JavaScript

## Como executar o projeto

### 1 - Pré Requisitos
Você deverá ter instalado em sua máquina:
- Python
- Git (opcional, para clonar o repositório)
- Virtualenv (recomendado)

### 2 - Clonar o repositório

```bash
git clone https://github.com/raphaelmsf/todo_list.git
```

### 3 - Criar e ativar um ambiente virtual


```bash
python -m venv venv

#Ativar o ambiente virtual
#No Windows:
venv\Scripts\activate

#No Linux/macOS:
source venv/bin/activate
```

### 4 - Instalar Django

```bash
python -m pip install Django
```

### 5 - Rodar migrações no banco de dados

```bash
python manage.py migrate
```

### 6 - Criar um superusuario (opcional, para acesso ao admin)

```bash
python manage.py runserver
```
A aplicação estará disponível em http://127.0.0.1:8000 ou localhost:8000

o desenvolvimento da aplicação ainda se encontra em andamento, conforme mais funcionalidades são adicionadas, este arquivo será atualizado