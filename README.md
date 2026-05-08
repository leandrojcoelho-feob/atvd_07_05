# 🎬 Sistema de Gestão de Cinemas (atvd_07_05)

Projeto criado a partir de uma atividade em aula de Engenharia de Software.

Este sistema é uma aplicação de terminal desenvolvida em **Python** que simula a gestão de uma rede de cinemas. Ele permite cadastrar unidades de cinema, registrar filmes, organizar sessões e controlar a venda de ingressos (público) respeitando as regras de negócio de capacidade máxima.

---

## 🏗️ Arquitetura do Projeto

O projeto foi construído utilizando a arquitetura **MVC (Model-View-Controller)** combinada com os padrões **Service** e **Repository**. Essa separação de responsabilidades torna o código mais limpo, organizado e fácil de manter.

* **Model:** Define as entidades do domínio (Cinema, Filme, Sessão).
* **Repository:** Isola a lógica de acesso ao banco de dados (SQLite). Nenhuma regra de negócio fica aqui.
* **Service:** O "cérebro" do sistema. Contém as regras de negócio (ex: validar se o público não excede a capacidade do cinema).
* **Controller:** Faz a ponte entre a interface (View) e a lógica (Service).
* **View (`main.py`):** A interface de interação com o usuário através do terminal.

### **Estrutura de Arquivos ->**
```text
atvd_07_05/
│
├── models/
│   └── models.py        # Entidades de dados
├── repository/
│   └── repository.py    # Comunicação com o SQLite
├── service/
│   └── service.py       # Validações e Regras de Negócio
├── controller/
│   └── controller.py    # Orquestração de chamadas
└── main.py              # Menu interativo (View) e inicialização

```

---

## ✨ Funcionalidades

O sistema conta com um menu interativo que permite:

1. **Cadastrar Cinemas:** Nome, capacidade máxima de público e endereço.
2. **Cadastrar Filmes:** Título, duração, diretor e gênero.
3. **Criar Sessões:** Vincula um filme a um cinema em uma data e hora específicas.
4. **Registrar Público:** Adiciona o número de espectadores a uma sessão (com validação de capacidade máxima do local).
5. **Consultas:**
* Listar todos os Cinemas.
* Listar todos os Filmes.
* Consultar Sessões detalhadas (com cruzamento de dados mostrando o nome do filme e do cinema).
* Filtrar as sessões de um cinema específico.



---

## 🚀 Como Executar o Projeto

O projeto foi desenvolvido para ser simples e não requer a instalação de bibliotecas externas complexas, utilizando apenas as bibliotecas nativas do Python (`sqlite3`, `dataclasses`).

### Pré-requisitos

* **Python 3.x** instalado na sua máquina.

### Passo a Passo

1. **Clone este repositório** (ou baixe os arquivos):
```bash
git clone [https://github.com/SEU_USUARIO/atvd_07_05.git](https://github.com/SEU_USUARIO/atvd_07_05.git)

```


2. **Acesse a pasta do projeto:**
```bash
cd atvd_07_05

```


3. **Execute o arquivo principal:**
```bash
python main.py

```



> **Nota:** Ao rodar o sistema pela primeira vez, o próprio código se encarregará de criar o arquivo do banco de dados (`cinema.db`) e montar todas as tabelas necessárias automaticamente.
