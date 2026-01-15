# 13. Create a RESTful Flask API for a Product resource with endpoints to:
# Add a product
# Get all products
# Get a product by ID
# Update a product
# Delete a product
from flask import Flask,request,render_template,jsonify,redirect,url_for #type:ignore
app = Flask(__name__)
products = []
product_id_counter = 1

# Add new product
@app.route('/product',methods=['POST'])
def add_product():
    global product_id_counter

    data = request.get_json()
    product = {
        'id':product_id_counter,
        'name' :data.get['name'],
        'price' :product.get['price']
    }
    products.append(product)
    product_id_counter += 1
    return jsonify(product),201

# Get all product
@app.route('/product',methods=['GET'])
def get_product():
    return jsonify(products)

# get a specific product
@app.route('/product<int:product_id>',methods=['GET'])
def get_products(product_id):
    for product in products:
        if product['id'] == product_id:
            return jsonify(product),200
    return jsonify({'Error':'PRoduct not found'}),404

# Update a product
@app.route('/product<int:product_id>',methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    for product in products:
        if product['id'] == product_id:
            product['name'] = data.get('name',product['name'])
            product['price'] = data.get('price',product['price'])
            return jsonify(product)
    return jsonify({'Error':'Product not found'}),404

# Delete The product
@app.route('/product<product_id>',methods=['DELETE'])
def delete_product(product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return jsonify({'message':'product delted'})
    return jsonify({'Error':"Product not found"})

if __name__ == '__main__':
    app.run()
