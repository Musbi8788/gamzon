from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)