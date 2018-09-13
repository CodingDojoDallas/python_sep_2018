from flask import Flask, render_template
app = Flask(__name__)  

print(__name__)
@app.route("/")
def Index():
    return render_template('checkerboard.html', x=8, y=8)

@app.route("/<int:x>/<int:y>")
def Checkerboard(x,y):
    return render_template('checkerboard.html', x=x, y=y)

if __name__=="__main__":
    app.run(debug=True)  