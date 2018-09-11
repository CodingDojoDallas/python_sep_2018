from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)

@app.route('/')
def store():
    return render_template("index.html")

@app.route('/checkout', methods = ["POST"])
def checkout():
    total = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    x = datetime.datetime.now().strftime("%c")
    print('Strawberry', request.form['strawberry'])
    print('Raspberry', request.form['raspberry'])
    print('Apple', request.form['apple'])
    print('Name', request.form['name'])
    print('ID', request.form['id'])
    return render_template("checkout.html", tot = total, date = x)


app.run(debug=True)