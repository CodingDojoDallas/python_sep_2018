from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')

def Draw():
    return render_template("index.html")

@app.route('/<x>/<y>')
def reDraw(x, y):
    return render_template("redraw.html", row = int(x), column = int(y))

app.run(debug=True)