from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def create_user():
    return render_template("form.html")

app.run(debug=True)