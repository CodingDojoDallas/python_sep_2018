from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
	return 'Hello World!'
@app.route('/play/<times>/<colors>')
def box(times,colors):
    return render_template("index.html", times= int(times), colors=colors)
if __name__=="__main__":
    app.run(debug=True)