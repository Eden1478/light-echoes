from flask import Flask, render_template
import stripe

app = Flask(__name__)

stripe.api_key = 'Ypk_test_51N7gsaHBOaMqUausnnLkrVyBmcX3eKKLPxIzZYKsLr8806rocGRZvslZ5nvRaz04CR3Az2OMyNYEIZgXDoLVwfu200u3wyDkPw'

@app.route('/pay')
def payment():
    return render_template('payment.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__=='__main__':
    app.run(debug=True)
