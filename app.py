from flask import Flask
from models import db, Product
from routes import bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orders.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(bp)

with app.app_context():
    db.create_all()

    if not Product.query.first():
        products = [
            Product(name="Pen Bic", category="Writing Goods", stock=100, price = 10.50),
            Product(name="A4 Paper", category="Paper Goods", stock=200, price = 30.00),
            Product(name="Notebook", category="Paper Goods", stock=150, price = 25.95),
            Product(name="Eraser", category="Accessories", stock=300, price = 0.95),
        ]
        db.session.add_all(products)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
