# Alchemy Order API
A RESTful API for managing products and orders, built with Flask and SQLAlchemy. Includes automated testing and CI/CD using GitHub Actions and Docker.

## 🚀 Features

- 📦 Manage Products (Create, Read, Update, Delete)
- 🛒 Manage Orders with stock validation
- 🧪 Unit tested with `pytest`
- 🐳 Dockerized for deployment
- 🔄 CI/CD pipeline via GitHub Actions
- 💾 SQLite (local)

## 📂 Project Structure

- `app.py` – App factory entry point  
- `main.py` – Application runner  
- `models.py` – SQLAlchemy models  
- `routes.py` – API routes and business logic  
- `seed.py` – DB seeder script to populate the database  
- `test_app.py` – Pytest test suite for CI/CD  
- `requirements.txt` – Python dependencies  
- `Dockerfile` – Docker image setup  
- `.github/workflows/ci.yml` – GitHub Actions CI/CD pipeline  
- `README.md` – Project documentation  






