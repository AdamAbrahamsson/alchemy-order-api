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

## 🛠️ Setup & Installation

### 📦 Local Setup (Python)

```bash
# Clone the repository
git clone https://github.com/AdamAbrahamsson/alchemy-order-api.git
cd alchemy-order-api

# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Seed the database
python3 seed.py

# Run the application
python3 main.py
```
### 🐳 Docker Setup
- **Build the image**

    ```bash
    docker build -t alchemy-order-api .
    ```


- **You have the option to pull the image**

    ```bash
    docker pull adamabrahamsson/alchemy-order-api:latest
    ```

- **Run the container (port 5001 used inside Dockerfile)**

    ```bash
    docker run -p 5001:5000 alchemy-order-api
    ```

###🔬 Running Tests
- **Running the test in the IDE**
    ```bash
    pytest
    ```
- **Running the test in the docker image**
    ```bash
    docker run --rm alchemy-order-api pytest
    ```



















