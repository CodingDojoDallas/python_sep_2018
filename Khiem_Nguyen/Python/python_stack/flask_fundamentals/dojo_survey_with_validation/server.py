from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def createUserResult():
    if len(request.form["name"]) < 1:
        flash("Name cannot be empty!")

    if len(request.form["comment"]) < 1:
        flash("Comments cannot be empty")

    if len(request.form["comment"]) > 120:
        flash("A comment cannot have more than 120 characters")

    if "_flashes" in session.keys():
        return redirect("/")

    else:
        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
    return render_template("result.html")

@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/danger")
def danger():
    print("a user tried to vist /danger")
    return redirect(url_for("/"))








if __name__=="__main__":
    app.run(debug=True)
