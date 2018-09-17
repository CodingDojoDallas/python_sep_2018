from flask import Flask, render_template, request, redirect, session

import random

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "location" not in session:
        session["location"] = ""
    if "findgold" not in session:
        session["findgold"] = 0
    if "string" not in session:
        session["string"] = ""

    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process():
    if request.form["location"] == "farm":
        session["findgold"] = random.randrange(10,21)
        session["string"] += "/n" + "Earned " + str(session["findgold"]) + "golds from the farm!"
        session["gold"] += int(session["findgold"])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
