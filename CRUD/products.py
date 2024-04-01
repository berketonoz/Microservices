from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

@app.route('/products', methods=["GET"])
def get_products():
    return jsonify(products)

@app.route('/products/<id>', methods=["GET"])
def get_product(id):
    product =  [ p for p in products if p['id'] == int(id)]
    if len(product) > 0:
        product = product[0]
        return product
    return '', 404

@app.route('/products', methods=["POST"])
def add_product():
    try:
        products.append(request.get_json())
    except:
        return '', 400
    return '', 201

@app.route('/products/<id>', methods=["PUT"])
def update_product(id):
    updated_product = request.get_json()
    product = [ p for p in products if p['id'] == int(id)]
    if len(product) > 0:
        product = product[0]
        for k in updated_product.keys(): 
            product[k] = updated_product[k]
        return product, 200
    return '', 204

@app.route('/products/<id>', methods=["DELETE"])
def delete_product(id):
    product = [ p for p in products if p['id'] == int(id)]
    if len(product) > 0:
        product = product[0]
        try:
            products.remove(product)
        except:
            return '', 400
    return '', 200

app.run(port=5000,debug=True)
