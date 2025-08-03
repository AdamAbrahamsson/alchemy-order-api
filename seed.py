from app import create_app
from models import db, Product

app = create_app()

with app.app_context():
    if not Product.query.first():
        products = [
            Product(name="Pen Bic", category="Writing Goods", stock=100, price=10.50),
            Product(name="A4 Paper", category="Paper Goods", stock=200, price=30.00),
            Product(name="Notebook", category="Paper Goods", stock=150, price=25.95),
            Product(name="Eraser", category="Accessories", stock=300, price=0.95),
        ]
        db.session.add_all(products)
        db.session.commit()
