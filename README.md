# APIs REST - Django REST Framework

### Seminário de Sistemas - CEUB - Análise e Desenvolvimento de Sistemas

Projeto com 6 APIs REST desenvolvidas em Python, Django e Django REST Framework. A solução foi organizada em camadas de models, serializers, views e rotas, com persistência em banco SQLite para desenvolvimento local.

---

## Estrutura do Projeto

```text
projeto_apis/
|-- manage.py
|-- settings.py
|-- urls.py
|-- requirements.txt
|-- .gitignore
|-- docs/
|   |-- diagrama.md
|   |-- diagrama_banco.mmd
|   `-- diagrama_banco.svg
|-- sistema_financeiro/
|   |-- models.py        # Categoria, Despesa, Receita
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   `-- apps.py
|-- sistema_academia/
|   |-- models.py        # Aluno, Plano, Matricula
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   `-- apps.py
|-- sistema_clinica/
|   |-- models.py        # Medico, Paciente, Consulta
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   `-- apps.py
|-- sistema_oficina/
|   |-- models.py        # Cliente, Veiculo, OrdemServico
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   `-- apps.py
|-- sistema_passagens/
|   |-- models.py        # Aeroporto, Voo, Passagem
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   `-- apps.py
`-- sistema_hospital/
    |-- models.py        # Especialidade, Medico, Paciente, AgendamentoConsulta
    |-- serializers.py
    |-- views.py
    |-- urls.py
    `-- apps.py
```

---

## Diagrama do Banco de Dados

O diagrama ERD do projeto está na pasta `docs/`:

- [docs/diagrama.md](docs/diagrama.md) - versão em Mermaid, renderizada pelo GitHub.
- [docs/diagrama_banco.svg](docs/diagrama_banco.svg) - versão visual para abrir direto no navegador.
- [docs/diagrama_banco.mmd](docs/diagrama_banco.mmd) - código-fonte Mermaid do diagrama.

---

## Tecnologias Utilizadas

| Componente | Tecnologia |
|---|---|
| Linguagem | Python 3.11+ |
| Framework Web | Django 4.2+ |
| Framework de API | Django REST Framework 3.15+ |
| Banco de Dados | SQLite |
| ORM | Django ORM |
| Padrão de API | REST com ModelViewSet + DefaultRouter |

---

## Como Rodar Localmente

### 1. Criar e ativar o ambiente virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac:

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Criar o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar superusuário

```bash
python manage.py createsuperuser
```

### 5. Rodar o servidor

```bash
python manage.py runserver
```

Acesse em:

```text
http://127.0.0.1:8000/
```

---

## Endpoints Disponíveis

### Sistema Financeiro Pessoal - `/api/financeiro/`

| Método | Endpoint | Ação |
|---|---|---|
| GET / POST | `/api/financeiro/categorias/` | Listar / Criar categoria |
| GET / PUT / PATCH / DELETE | `/api/financeiro/categorias/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/financeiro/despesas/` | Listar / Criar despesa |
| GET / PUT / PATCH / DELETE | `/api/financeiro/despesas/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/financeiro/receitas/` | Listar / Criar receita |
| GET / PUT / PATCH / DELETE | `/api/financeiro/receitas/{id}/` | Detalhar / Editar / Excluir |

### Sistema de Academia - `/api/academia/`

| Método | Endpoint | Ação |
|---|---|---|
| GET / POST | `/api/academia/alunos/` | Listar / Criar aluno |
| GET / PUT / PATCH / DELETE | `/api/academia/alunos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/academia/planos/` | Listar / Criar plano |
| GET / PUT / PATCH / DELETE | `/api/academia/planos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/academia/matriculas/` | Listar / Criar matrícula |
| GET / PUT / PATCH / DELETE | `/api/academia/matriculas/{id}/` | Detalhar / Editar / Excluir |

### Sistema de Clínica Médica - `/api/clinica/`

| Método | Endpoint | Ação |
|---|---|---|
| GET / POST | `/api/clinica/medicos/` | Listar / Criar médico |
| GET / PUT / PATCH / DELETE | `/api/clinica/medicos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/clinica/pacientes/` | Listar / Criar paciente |
| GET / PUT / PATCH / DELETE | `/api/clinica/pacientes/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/clinica/consultas/` | Listar / Agendar consulta |
| GET / PUT / PATCH / DELETE | `/api/clinica/consultas/{id}/` | Detalhar / Editar / Cancelar |

### Sistema de Oficina Mecânica - `/api/oficina/`

| Método | Endpoint | Ação |
|---|---|---|
| GET / POST | `/api/oficina/clientes/` | Listar / Criar cliente |
| GET / PUT / PATCH / DELETE | `/api/oficina/clientes/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/oficina/veiculos/` | Listar / Criar veículo |
| GET / PUT / PATCH / DELETE | `/api/oficina/veiculos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/oficina/ordens-servico/` | Listar / Abrir ordem de serviço |
| GET / PUT / PATCH / DELETE | `/api/oficina/ordens-servico/{id}/` | Detalhar / Editar / Fechar |

### Sistema de Passagens Aéreas - `/api/passagens/`

| Método | Endpoint | Ação |
|---|---|---|
| GET / POST | `/api/passagens/aeroportos/` | Listar / Criar aeroporto |
| GET / PUT / PATCH / DELETE | `/api/passagens/aeroportos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/passagens/voos/` | Listar / Criar voo |
| GET / PUT / PATCH / DELETE | `/api/passagens/voos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/passagens/passagens/` | Listar / Emitir passagem |
| GET / PUT / PATCH / DELETE | `/api/passagens/passagens/{id}/` | Detalhar / Editar / Cancelar |

### Sistema de Hospital Público - `/api/hospital/`

| Método | Endpoint | Ação |
|---|---|---|
| GET / POST | `/api/hospital/especialidades/` | Listar / Criar especialidade |
| GET / PUT / PATCH / DELETE | `/api/hospital/especialidades/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/hospital/medicos/` | Listar / Criar médico |
| GET / PUT / PATCH / DELETE | `/api/hospital/medicos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/hospital/pacientes/` | Listar / Criar paciente |
| GET / PUT / PATCH / DELETE | `/api/hospital/pacientes/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/hospital/agendamentos/` | Listar / Agendar consulta |
| GET / PUT / PATCH / DELETE | `/api/hospital/agendamentos/{id}/` | Detalhar / Editar / Cancelar |

---

## Relação com os Requisitos do Seminário

| Requisito | Onde está implementado |
|---|---|
| Diagrama | `docs/diagrama.md` e `docs/diagrama_banco.svg` |
| Models | `models.py` em cada app |
| Serializers | `serializers.py` em cada app |
| Views | `views.py` com `ModelViewSet` |
| Rotas/URLs | `urls.py` em cada app e `urls.py` principal |
| Banco de dados | `settings.py` com SQLite e migrations de cada app |
| CRUDs/APIs | 19 recursos REST com list/create/detail/update/delete |

---

## Como Subir no GitHub

Crie um repositório público no GitHub e execute os comandos abaixo dentro da pasta do projeto:

```bash
git init
git add .
git commit -m "projeto APIs REST Django"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/apis-rest-seminario.git
git push -u origin main
```

Substitua `SEU_USUARIO` pelo seu usuário do GitHub.

---

## Desenvolvido Para

Seminário de Sistemas - CEUB - Análise e Desenvolvimento de Sistemas.
