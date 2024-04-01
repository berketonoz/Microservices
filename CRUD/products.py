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


app.run(port=5000,debug=True)
