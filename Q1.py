###QUESTION ONE: Django Models for E-Commerce
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
### QUESTION TWO: REST API for Products

#### app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for simplicity
products = []

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    product = {
        'id': len(products) + 1,
        'name': data['name'],
        'description': data.get('description', ''),
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)

#### Python Client Script

import requests

BASE_URL = 'http://127.0.0.1:5000/products'

# Add new product
product_data = {
    'name': 'Laptop',
    'description': 'High-performance laptop',
    'price': 1200.99
}
response = requests.post(BASE_URL, json=product_data)
print('Product Creation Response:', response.json())

# Get all products
response = requests.get(BASE_URL)
print('Product List:', response.json())


