from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True) # Every product will have a unique ID
    name = db.Column(db.String(100), nullable=False) # Product name (required)
    category = db.Column(db.String(50), nullable=True) # Product category (optional)
    stock = db.Column(db.Integer, nullable=False) # Quantity in stock (required)
    price = db.Column(db.Float, nullable=False) # Product price (required)

    def __repr__(self):
        return f"<Product {self.name} ({self.category})>"
