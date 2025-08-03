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