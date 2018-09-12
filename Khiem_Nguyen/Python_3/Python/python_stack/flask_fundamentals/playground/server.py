from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template("index.html", times=int(3))

@app.route("/play/<x>")
def createBox(x):
    return render_template("index.html", times=int(x))

@app.route("/play/<x>/<color>")
def createBoxandColor(x,color):
    return render_template("index.html", times=int(x), box_color=color)





if __name__=="__name__":
    app.run(debug=True)
