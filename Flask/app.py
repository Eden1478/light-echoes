from flask import Flask, render_template
import datetime

time = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html', time = datetime.datetime.now())

@app.route('/contact')
def contact():
    return render+render_template('contact.html')
                                  
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name = name)





if __name__=='__main__':
    app.run(debug=True)