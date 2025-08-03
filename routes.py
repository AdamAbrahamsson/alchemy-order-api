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

@bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": f"Product with ID {product_id} not found."}), 404
    
    return jsonify({
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "stock": product.stock,
        "price": product.price
    }), 200

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

@bp.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    required_fields = {
        "name": str,
        "category": str,
        "stock": int,
        "price": (int, float)
    }
    errors = {}

    # Unexpected fields
    for key in data.keys():
        if key not in required_fields:
            errors[key] = "Unexpected field."

    # Validate required fields and types
    for field, field_type in required_fields.items():
        if field not in data:
            errors[field] = "Missing required field."
        else:
            if not isinstance(data[field], field_type):
                errors[field] = f"Invalid type. Expected {field_type}."

    # Check for duplicate product name
    existing = Product.query.filter_by(name=data.get("name")).first()
    if existing:
        errors["name"] = "Product with this name already exists."

    if errors:
        return jsonify({"errors": errors}), 400

    # Create and add new product
    new_product = Product(
        name=data["name"],
        category=data["category"],
        stock=data["stock"],
        price=data["price"]
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully."}), 201

@bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    deleted_name = product.name
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({"message": "Product deleted successfully."}), 200
