# 🍽️ Meal API – CRUD de Refeições (Projeto de Estudo)

Este projeto é uma **API REST simples em Flask** para gerenciamento de refeições, desenvolvida com o objetivo de **praticar conceitos de CRUD, Flask e SQLAlchemy** durante meus estudos.
> Este não é um projeto principal do meu GitHub. Ele foi criado **apenas para fins de fixação de conteúdo**.
> Já possuo um CRUD mais completo e estruturado em outro repositório.

---

## 🚀 Tecnologias utilizadas

* Python 3
* Flask
* Flask-SQLAlchemy
* MySql
* python-dotenv

---

## 📌 Funcionalidades

* ✅ Criar uma refeição
* 📄 Listar refeições por usuário
* 🔍 Buscar uma refeição por ID
* ✏️ Atualizar uma refeição
* ❌ Deletar uma refeição

Cada refeição está associada a um `user_id`, que é armazenado diretamente na tabela de refeições.

---

## 📂 Estrutura básica do projeto

```
.
├── app.py
├── database.py
├── model/
│   └── meal.py
├── .env
└── README.md
```

---

## ⚙️ Configuração do ambiente

### 1️⃣ Clonar o repositório

```bash
git clone <url-do-repositorio>
cd nome-do-projeto
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install flask flask-sqlalchemy python-dotenv
```

### 4️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta
CONNECTION_DB=sqlite:///database.db
```

---

## ▶️ Executando o projeto

```bash
python app.py
```

A API estará disponível em:

```
http://localhost:5000
```

---

## 🧪 Rotas da API

### ➕ Criar refeição

**POST** `/meal/register`

```json
{
  "name": "Almoço",
  "description": "Arroz, feijão e frango",
  "datetime": "10-01-2025 12:30:00",
  "is_on_diet": true,
  "user_id": 1
}
```

---

### 📄 Listar refeições por usuário

**GET** `/meal/meals/<user_id>`

---

### 🔍 Buscar refeição por ID

**GET** `/meal/<meal_id>`

---

### ✏️ Atualizar refeição

**PUT** `/meal/<meal_id>`

```json
{
  "name": "Jantar",
  "description": "Salada",
  "datetime": "10-01-2025 19:00:00",
  "is_on_diet": true
}
```

---

### ❌ Deletar refeição

**DELETE** `/meal/<meal_id>`

---

## 📚 Observações finais

* Projeto desenvolvido **exclusivamente para estudo**
* Não possui autenticação
* Não possui tabela de usuários
* Código simples e direto para facilitar o aprendizado

---

## 👤 Autor

Desenvolvido por **[MATHEUS GOMES]**

