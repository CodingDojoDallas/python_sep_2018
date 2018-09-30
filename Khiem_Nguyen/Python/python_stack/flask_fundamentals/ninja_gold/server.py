from flask import Flask, render_template, request, redirect, session

import random
from datetime import datetime, date, time

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    if "currentgold" not in session:
        session["currentgold"] = 0
    if "location" not in session:
        session["location"] = ""
    if "findgold" not in session:
        session["findgold"] = 0
    if "string" not in session:
        session["string"] = ""

    return render_template("index.html", currentgold =session["currentgold"], string = session["string"])

@app.route("/process_money", methods=["POST"])
def process():
    if request.form["location"] == "farm":
        session["findgold"] = random.randrange(10,21)
        session["string"] += "\n" + "Earned " + str(session["findgold"]) + " golds from the farm!  " + str(datetime.today())
        session["currentgold"] += int(session["findgold"])
    if request.form["location"] == "cave":
        session["findgold"] = random.randrange(5,11)
        session["string"] += "\n" + "Earned " + str(session["findgold"]) + " golds from the cave! " + str(datetime.today())
        session["currentgold"] += int(session["findgold"])
    if request.form["location"] == "house":
        session["findgold"] = random.randrange(2,6)
        session["string"] += "\n" + "Earned " + str(session["findgold"]) + " golds from the house! " + str(datetime.today())
        session["currentgold"] += int(session["findgold"])
    if request.form["location"] == "casino":
        session["findgold"] = random.randrange(-50,51)
        session["string"] += "\n" + "Earned " + str(session["findgold"]) + " golds from the casino! " + str(datetime.today())
        session["currentgold"] += int(session["findgold"])
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
