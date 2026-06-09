# APIs REST — Django REST Framework
### Seminário de Sistemas · CEUB · Análise e Desenvolvimento de Sistemas

Projeto com **6 APIs REST** desenvolvidas em Python com Django e Django REST Framework.

---

## 📁 Estrutura do Projeto

```
projeto_apis/
│
├── manage.py
├── settings.py
├── urls.py
├── requirements.txt
├── .gitignore
│
├── sistema_financeiro/
│   ├── models.py        # Categoria, Despesa, Receita
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
│
├── sistema_academia/
│   ├── models.py        # Aluno, Plano, Matricula
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
│
├── sistema_clinica/
│   ├── models.py        # Medico, Paciente, Consulta
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
│
├── sistema_oficina/
│   ├── models.py        # Cliente, Veiculo, OrdemServico
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
│
├── sistema_passagens/
│   ├── models.py        # Aeroporto, Voo, Passagem
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
│
└── sistema_hospital/
    ├── models.py        # Especialidade, Medico, Paciente, AgendamentoConsulta
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── apps.py
```

---

## 🚀 Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

### 2. Criar e ativar o ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar superusuário (para acessar o admin)

```bash
python manage.py createsuperuser
```

### 6. Rodar o servidor

```bash
python manage.py runserver
```

Acesse em: **http://127.0.0.1:8000/**

---

## 🔗 Endpoints disponíveis

### 💰 Sistema Financeiro Pessoal — `/api/financeiro/`

| Método | Endpoint | Ação |
|--------|----------|------|
| GET / POST | `/api/financeiro/categorias/` | Listar / Criar categoria |
| GET / PUT / DELETE | `/api/financeiro/categorias/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/financeiro/despesas/` | Listar / Criar despesa |
| GET / PUT / DELETE | `/api/financeiro/despesas/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/financeiro/receitas/` | Listar / Criar receita |
| GET / PUT / DELETE | `/api/financeiro/receitas/{id}/` | Detalhar / Editar / Excluir |

### 🏋️ Sistema de Academia — `/api/academia/`

| Método | Endpoint | Ação |
|--------|----------|------|
| GET / POST | `/api/academia/alunos/` | Listar / Criar aluno |
| GET / PUT / DELETE | `/api/academia/alunos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/academia/planos/` | Listar / Criar plano |
| GET / PUT / DELETE | `/api/academia/planos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/academia/matriculas/` | Listar / Criar matrícula |
| GET / PUT / DELETE | `/api/academia/matriculas/{id}/` | Detalhar / Editar / Excluir |

### 🏥 Sistema de Clínica Médica — `/api/clinica/`

| Método | Endpoint | Ação |
|--------|----------|------|
| GET / POST | `/api/clinica/medicos/` | Listar / Criar médico |
| GET / PUT / DELETE | `/api/clinica/medicos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/clinica/pacientes/` | Listar / Criar paciente |
| GET / PUT / DELETE | `/api/clinica/pacientes/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/clinica/consultas/` | Listar / Agendar consulta |
| GET / PUT / DELETE | `/api/clinica/consultas/{id}/` | Detalhar / Editar / Cancelar |

### 🔧 Sistema de Oficina Mecânica — `/api/oficina/`

| Método | Endpoint | Ação |
|--------|----------|------|
| GET / POST | `/api/oficina/clientes/` | Listar / Criar cliente |
| GET / PUT / DELETE | `/api/oficina/clientes/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/oficina/veiculos/` | Listar / Criar veículo |
| GET / PUT / DELETE | `/api/oficina/veiculos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/oficina/ordens-servico/` | Listar / Abrir OS |
| GET / PUT / DELETE | `/api/oficina/ordens-servico/{id}/` | Detalhar / Editar / Fechar |

### ✈️ Sistema de Passagens Aéreas — `/api/passagens/`

| Método | Endpoint | Ação |
|--------|----------|------|
| GET / POST | `/api/passagens/aeroportos/` | Listar / Criar aeroporto |
| GET / PUT / DELETE | `/api/passagens/aeroportos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/passagens/voos/` | Listar / Criar voo |
| GET / PUT / DELETE | `/api/passagens/voos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/passagens/passagens/` | Listar / Emitir passagem |
| GET / PUT / DELETE | `/api/passagens/passagens/{id}/` | Detalhar / Editar / Cancelar |

### 🏨 Sistema de Hospital Público — `/api/hospital/`

| Método | Endpoint | Ação |
|--------|----------|------|
| GET / POST | `/api/hospital/especialidades/` | Listar / Criar especialidade |
| GET / PUT / DELETE | `/api/hospital/especialidades/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/hospital/medicos/` | Listar / Criar médico |
| GET / PUT / DELETE | `/api/hospital/medicos/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/hospital/pacientes/` | Listar / Criar paciente |
| GET / PUT / DELETE | `/api/hospital/pacientes/{id}/` | Detalhar / Editar / Excluir |
| GET / POST | `/api/hospital/agendamentos/` | Listar / Agendar consulta |
| GET / PUT / DELETE | `/api/hospital/agendamentos/{id}/` | Detalhar / Editar / Cancelar |

---

## 📤 Como subir no GitHub (passo a passo)

### Passo 1 — Criar o repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login
2. Clique em **"New repository"** (botão verde no canto superior direito)
3. Dê um nome ao repositório (ex: `apis-rest-seminario`)
4. Deixe como **Public**
5. **Não** marque nenhuma opção extra (README, .gitignore, etc.)
6. Clique em **"Create repository"**

---

### Passo 2 — Inicializar o Git na pasta do projeto

Abra o terminal **dentro da pasta `projeto_apis`** e rode:

```bash
git init
git add .
git commit -m "primeiro commit - projeto APIs REST Django"
```

---

### Passo 3 — Conectar ao repositório do GitHub

Copie a URL do seu repositório (aparece na página após criar) e rode:

```bash
git remote add origin https://github.com/SEU_USUARIO/apis-rest-seminario.git
git branch -M main
git push -u origin main
```

> Substitua `SEU_USUARIO` e `apis-rest-seminario` pelo seu usuário e nome do repositório.

---

### Passo 4 — Verificar

Acesse seu repositório no GitHub e confirme que todos os arquivos foram enviados.

---

### Como atualizar o repositório depois de fazer alterações

Sempre que modificar algum arquivo:

```bash
git add .
git commit -m "descreva o que mudou aqui"
git push
```

---

## 🛠️ Stack Tecnológica

| Componente | Tecnologia |
|---|---|
| Linguagem | Python 3.11+ |
| Framework Web | Django 4.2+ |
| Framework de API | Django REST Framework 3.15+ |
| Banco de Dados | SQLite (desenvolvimento) |
| ORM | Django ORM |
| Padrão | REST — ModelViewSet + DefaultRouter |

---

## 👨‍💻 Desenvolvido para

Seminário de Sistemas — CEUB · Análise e Desenvolvimento de Sistemas
