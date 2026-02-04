# 🏛️ Salvattore Assessoria

<p align="center">
  <strong>Transformando a gestão pública com inovação e eficiência</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.1.2-green?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

---

## 📋 Sobre o Projeto

O **Salvattore Assessoria** é uma aplicação web desenvolvida em Flask para uma consultoria especializada em gestão pública e educacional. O sistema oferece uma plataforma completa para apresentação de serviços, gerenciamento de processos seletivos e comunicação com clientes.

### 🎯 Principais Funcionalidades

- **📄 Página Institucional** - Apresentação da empresa, missão e serviços oferecidos
- **📬 Formulário de Contato** - Permite que visitantes enviem mensagens que são armazenadas em CSV
- **📋 Processos Seletivos** - Listagem de processos seletivos abertos ao público
- **📅 Agendamentos** - Página para agendamento de serviços
- **🔐 Painel Administrativo** - Sistema de login para gerenciamento de processos seletivos (CRUD completo)

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Python** | 3.x | Linguagem de programação |
| **Flask** | 3.1.2 | Framework web |
| **Jinja2** | 3.1.6 | Template engine |
| **Werkzeug** | 3.1.4 | Biblioteca WSGI |
| **python-dotenv** | - | Gerenciamento de variáveis de ambiente |
| **HTML5/CSS3** | - | Frontend |
| **Font Awesome** | 6.0.0 | Ícones |

---

## 📁 Estrutura do Projeto

```
salvattore-projeto-IES/
│
├── 📄 app.py                    # Arquivo principal da aplicação Flask
├── 📄 requirements.txt          # Dependências do projeto
├── 📄 README.md                 # Documentação
├── 📄 LICENSE                   # Licença do projeto
│
├── 📁 admin/                    # Módulo administrativo (Blueprint)
│   ├── __init__.py              # Inicialização do Blueprint
│   └── routes.py                # Rotas do painel admin
│
├── 📁 data/                     # Armazenamento de dados
│   ├── dados.csv                # Mensagens de contato
│   └── processos.csv            # Processos seletivos
│
├── 📁 static/                   # Arquivos estáticos
│   ├── 📁 css/
│   │   └── style.css            # Estilos da aplicação
│   └── 📁 images/               # Imagens e logos
│
└── 📁 templates/                # Templates HTML
    ├── base.html                # Template base
    ├── index.html               # Página inicial
    ├── contato.html             # Formulário de contato
    ├── processos.html           # Lista de processos
    ├── agendamentos.html        # Página de agendamentos
    │
    └── 📁 admin/                # Templates administrativos
        ├── login.html           # Página de login
        ├── gerenciar_processos.html  # Gerenciamento
        ├── criar_processo.html  # Criar novo processo
        └── editar_processo.html # Editar processo
```

---

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)
- Git (opcional)

### Passo a Passo

#### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/salvattore-projeto-IES.git
cd salvattore-projeto-IES
```

#### 2️⃣ Crie um ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SALVATTORE_ADMIN=seu_usuario_admin
SALVATTORE_SENHA=sua_senha_segura
```

#### 5️⃣ Execute a aplicação

```bash
python app.py
```

A aplicação estará disponível em: **http://127.0.0.1:5000**

---

## 📖 Rotas da Aplicação

### Rotas Públicas

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/contato` | GET, POST | Formulário de contato |
| `/processos` | GET | Lista de processos seletivos |
| `/agendamentos` | GET | Página de agendamentos |

### Rotas Administrativas

| Rota | Método | Descrição |
|------|--------|-----------|
| `/admin/login` | GET, POST | Login do administrador |
| `/admin/logout` | GET | Logout |
| `/admin/processos` | GET | Gerenciar processos |
| `/admin/novo` | GET, POST | Criar novo processo |
| `/admin/editar/<id>` | GET, POST | Editar processo |
| `/admin/deletar/<id>` | GET, POST | Deletar processo |

---

## 🔐 Painel Administrativo

O sistema possui um painel administrativo protegido por autenticação para gerenciar processos seletivos.

### Funcionalidades do Admin:
- ✅ Login/Logout seguro com sessão
- ✅ Criar novos processos seletivos
- ✅ Editar processos existentes
- ✅ Excluir processos
- ✅ Visualizar lista de processos

### Acesso:
1. Acesse `/admin/login`
2. Use as credenciais definidas no arquivo `.env`

---

## 💼 Serviços Oferecidos

A Salvattore Assessoria oferece os seguintes serviços:

- 🎓 **Consultoria em Educação** - Apoio ao planejamento e gestão educacional
- 👨‍🏫 **Formação para Professores** - Capacitação continuada com metodologias ativas
- 🏥 **Formação para Profissionais de Saúde** - Cursos e capacitações especializadas
- 📋 **Processos Seletivos** - Elaboração e execução de processos completos
- 📚 **Treinamentos** - Programas de desenvolvimento sob medida
- 🤝 **Assessoria Estratégica** - Consultoria de alto impacto em gestão pública

---

## 📝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📞 Contato

**Salvattore Assessoria**

- 📍 Localização: Patos, Paraíba - Brasil
- 📸 Instagram: [@salvattore.assessoria](https://www.instagram.com/salvattore.assessoria)

---

<p align="center">
  Feito com ❤️ para transformar a gestão pública brasileira
</p>
