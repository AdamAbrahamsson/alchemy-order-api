import pytest
from app import create_app
from models import db, Product

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
    assert len(data) == 2
    assert data[0]["name"] == "Pen"
    assert data[0]["category"] == "Writing"
    assert data[0]["stock"] == 100
    assert float(data[0]["price"]) == 1.5
