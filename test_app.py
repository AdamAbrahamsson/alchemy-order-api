import pytest
from app import create_app
from models import db, Product
import json

@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # In memmory database, not the local database
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            db.session.add(Product(name="Pen", category="Writing", stock=100, price=1.5))
            db.session.commit()
        yield client

def test_get_all_products(client):
    response = client.get("/products")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Pen"
    assert data[0]["category"] == "Writing"
    assert data[0]["stock"] == 100
    assert float(data[0]["price"]) == 1.5

def test_get_single_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200
    product = response.get_json()
    assert product["id"] == 1
    assert product["name"] == "Pen"

def test_get_nonexistent_product(client):
    response = client.get("/products/1000")
    assert response.status_code == 404
   
def test_create_product(client):
    new_product = {
        "name": "Notebook",
        "category": "Paper",
        "stock": 50,
        "price": 3.75
    }
    response = client.post("/products", data=json.dumps(new_product), content_type="application/json")
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Product added successfully."

    # Confirm count is now 2
    all_resp = client.get("/products")
    assert len(all_resp.get_json()) == 2

def test_update_product(client):
    update_data = {
        "stock": 80,
        "price": 2.00
    }
    response = client.patch("/products/1", data=json.dumps(update_data), content_type="application/json")
    assert response.status_code == 200
    updated = response.get_json()
    assert updated["stock"] == 80
    assert float(updated["price"]) == 2.00

def test_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 200

    # Confirm deleted
    get_resp = client.get("/products/1")
    assert get_resp.status_code == 404    
