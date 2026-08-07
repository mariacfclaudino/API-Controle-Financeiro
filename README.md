# Personal Finance API

A RESTful API for personal finance management, built with **FastAPI** and **SQLAlchemy**. Supports user registration, JWT authentication, and management of accounts, categories, and financial transactions.

## ✨ Features

- 🔐 JWT (JSON Web Token) user authentication
- 👤 User registration and login with encrypted passwords (bcrypt)
- 💰 Financial account management
- 🏷️ Category management
- 📊 Transaction recording and retrieval

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM
- [SQLite](https://www.sqlite.org/) — database
- [python-jose](https://github.com/mpdavis/python-jose) — JWT generation and validation
- [Passlib + bcrypt](https://passlib.readthedocs.io/) — password hashing
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [python-dotenv](https://github.com/theskumar/python-dotenv) — environment variables

## 📋 Requirements

- Python 3.10+
- pip

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/mariacfclaudino/API-Controle-Financeiro.git
cd API-Controle-Financeiro
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file with your own settings (see [Environment Variables](#-environment-variables)).

5. Run the application:
```bash
fastapi dev app/main.py
```

The API will be available at `http://127.0.0.1:8000`.

## 📖 Documentation

Once the application is running, interactive documentation is available at:

- **Swagger UI**: `http://127.0.0.1:8000/docs`

## 🔑 Environment Variables

Create a `.env` file in the project root with the following variables:

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Secret key used to sign JWT tokens | `your_random_secret_key` |
| `DATABASE_URL` | Database connection URL | `sqlite:///./financial.db` |
| `ALGORITHM` | JWT encryption algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time, in minutes | `30` |

## 🗂️ Project Structure

```
API-Controle-Financeiro/
├── app/
│   ├── auth/
│   │   ├── models.py       # User model
│   │   ├── schemas.py      # Pydantic schemas
│   │   └── router.py       # Login and user creation routes
│   ├── accounts/           # Account routes
│   │   ├── models.py       # Account model
│   │   ├── schemas.py      # Pydantic schemas
│   │   └── router.py       # Account creation routes
│   ├── categories/         # Category routes
│   │   ├── models.py       # Category model
│   │   ├── schemas.py      # Pydantic schemas
│   │   └── router.py       # Category routes
│   ├── transactions/       # Transaction routes
│   ├── database.py         # Database configuration
│   └── main.py              # Application entry point
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔌 Main Endpoints

| Method | Route | Description | Auth Required |
|---|---|---|---|
| POST | `/createuser` | Creates a new user | No |
| POST | `/login` | Authenticates and returns a JWT token | No |
| GET | `/accounts` | Lists user accounts | Yes |
| POST | `/accounts` | Creates a new account | Yes |
| GET | `/categories` | Lists categories | Yes |
| POST | `/categories` | Creates a new category | Yes |
| GET | `/transactions` | Lists transactions | Yes |
| POST | `/transactions` | Records a new transaction | Yes |

## 🔐 Authentication

After logging in, include the returned token in the header of protected requests:

```
Authorization: Bearer <your_token>
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

**Maria**
- GitHub: [@mariacfclaudino](https://github.com/mariacfclaudino)
