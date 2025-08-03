from flask import request, jsonify, Blueprint
from models import Product, db

bp = Blueprint('api', __name__)

@bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = [
        {
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "stock": p.stock,
            "price": p.price
        }
        for p in products
    ]
    return jsonify(result)

@bp.route('/products/<int:id>', methods=['Patch'])
def patch_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()

    if "stock" in data:
        product.stock = data["stock"]
    if "price" in data:
        product.price = data["price"]

    db.session.commit()

    return jsonify({
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "stock": product.stock,
        "price": product.price
    }), 200