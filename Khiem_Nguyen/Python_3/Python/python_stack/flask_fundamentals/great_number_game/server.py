from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "ThisIsSecret"

import random

@app.route("/")
def index():
    if "number" not in session:
        session["number"] = random.randrange(1, 101)

    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = request.form["guess"]
    if int(session["guess"]) == int(session["number"]):
        session["result"] = "correct"
    if int(session["guess"]) > int(session["number"]):
        session["result"] = "tooHigh"
    if int(session["guess"]) < int(session["number"]):
        session["result"] = "tooLow"
    return redirect('/')

@app.route("/reset")
def reset():
    session.pop("number")
    session.pop("result")
    session.pop("guess")
    return redirect("/")


    app.run(debug=True)
