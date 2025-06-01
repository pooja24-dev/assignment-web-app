from flask import Flask, render_template

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.00, 'image_url': 'https://assigmentstaticfilestore.blob.core.windows.net/assignment-images/product1.jpg'},
    {'id': 2, 'name': 'Product 2', 'price': 20.00, 'image_url': 'https://assigmentstaticfilestore.blob.core.windows.net/assignment-images/product2.jpg'},
    {'id': 3, 'name': 'Product 3', 'price': 30.00, 'image_url': 'https://assigmentstaticfilestore.blob.core.windows.net/assignment-images/product3.jpg'},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run()
