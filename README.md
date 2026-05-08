# 🎬 Sistema de Gestão de Cinemas (atvd_07_05)

Projeto criado a partir de uma atividade em aula.

Este sistema é uma aplicação interativa de terminal desenvolvida em **Python** que simula a gestão de uma rede de cinemas. O objetivo principal é demonstrar a aplicação da arquitetura **MVC (Model-View-Controller)** aliada aos padrões **Service** e **Repository**, garantindo separação de responsabilidades e facilitando a manutenção do código. O sistema também implementa o conceito de controle de acesso baseado em papéis, separando as funcionalidades por perfil de usuário.

---

## 🏗️ Arquitetura Utilizada

* **Models (`models.py`):** Define as entidades e estruturas de dados do domínio (Cinema, Filme, Sessão).
* **Repository (`repository.py`):** Isola toda a lógica de persistência e comunicação com o banco de dados SQLite. Nenhuma regra de negócio é tratada aqui.
* **Service (`service.py`):** Atua como o "cérebro" da aplicação, contendo todas as validações e regras de negócio (ex: garantir que o público não exceda a capacidade do cinema).
* **Controller (`controller.py`):** Faz a ponte e o roteamento entre as entradas do usuário (View) e as regras do sistema (Service).
* **View (`view/`):** Camada de apresentação dividida por perfis de acesso:
    * `view_func.py`: Interface exclusiva para funcionários (operações de escrita/cadastro).
    * `view_publico.py`: Interface para o público geral (operações de leitura/consulta).
* **Main (`main.py`):** Ponto de entrada e roteador principal da aplicação, responsável por identificar o perfil do usuário e direcioná-lo para a View correta.

**Estrutura ->**
```text
atvd_07_05/
│
├── models/
│   └── models.py
├── repository/
│   └── repository.py
├── service/
│   └── service.py
├── controller/
│   └── controller.py
├── view/
│   ├── view_func.py
│   └── view_publico.py
└── main.py

```

---

## ✨ Funcionalidades Principais

O sistema é dividido em dois grandes módulos de acesso:

**🔐 Painel do Funcionário (Requer Matrícula)**

* **Gestão de Cinemas:** Cadastro de novas unidades informando nome, capacidade e endereço.
* **Gestão de Filmes:** Cadastro do catálogo contendo título, duração, diretor e gênero.
* **Controle de Sessões:** Agendamento de exibições vinculando Filmes a Cinemas em datas e horários específicos.
* **Registro de Público:** Controle de venda de ingressos com validação estrita da capacidade máxima do local.

**🍿 Área do Público (Acesso Livre)**

* **Consultas Integradas:** * Listagem individual de Cinemas e Filmes em cartaz.
* Listagem geral de Sessões (cruzando dados para exibir os nomes do filme e do local).
* Filtro de Sessões específicas por ID do Cinema.



---

## 🚀 Como Executar

O projeto utiliza apenas bibliotecas nativas do Python (`sqlite3`, `dataclasses`), não sendo necessário instalar dependências externas complexas.

### Pré-requisitos

* **Python 3.x** instalado.

### Passos

1. Clone o repositório para a sua máquina local:
```bash
git clone [https://github.com/leandrojcoelho-feob/atvd_07_05.git](https://github.com/leandrojcoelho-feob/atvd_07_05.git)

```


2. Navegue até a pasta raiz do projeto:
```bash
cd atvd_07_05

```


3. Inicie a aplicação:
```bash
python main.py

```

> **Nota:** Na primeira execução, a aplicação inicializará automaticamente a configuração do SQLite, criando o arquivo de banco de dados (`cinema.db`) e todas as tabelas necessárias na raiz do projeto.

```
