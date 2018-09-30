from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def createUserResult():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template("result.html", name = name, location = location, language = language, comment = comment)

@app.route("/danger")
def danger():
    print("a user tried to vist /danger")
    return redirect(url_for("/"))








if __name__=="__main__":
    app.run(debug=True)
