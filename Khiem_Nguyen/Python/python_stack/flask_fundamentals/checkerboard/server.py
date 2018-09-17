from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", width=int(8), height=int(8))

@app.route("/<x>/<y>")
def create(x,y):
    return render_template("index.html", width=int(x), height=int(y))












if __name__=="__main__":
    app.run(debug=True)
