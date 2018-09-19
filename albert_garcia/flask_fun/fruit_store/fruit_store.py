from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)  

print(__name__)
@app.route('/')
def Index():
    return render_template('fruit_store.html')

@app.route('/checkout', methods =['POST'])
def Checkout():
    name = request.form['name']
    ids = request.form['ids']
    strawberry_quantity = request.form['strawberry_quantity']
    raspberry_quantity = request.form['raspberry_quantity']
    apple_quantity = request.form['apple_quantity']
    order = int(strawberry_quantity) + int(raspberry_quantity) + int(apple_quantity)
    x = datetime.now()
    time = x.strftime('%c')
    return render_template('fruit_store_checkout.html', order=order, time = time)

if __name__=="__main__":
    app.run(debug=True)