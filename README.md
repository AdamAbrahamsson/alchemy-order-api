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

alchemy-order-api/
  - app.py # App factory entry point
  - main.py # Application runner
  - models.py # SQLAlchemy model
  ─ routes.py # API routes and business logic
  ─ seed.py # DB seeder script to populate the database
  ─ test_app.py # Pytest test suite for the CI/CD
  ─ requirements.txt # Dependencies
  ─ Dockerfile # Docker image setup
  ─ .github/workflows/ # CI/CD pipeline config
    ─ ci.yml
  - README.md # This file




