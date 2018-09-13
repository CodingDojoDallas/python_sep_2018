from flask import Flask, render_template
app = Flask(__name__)

print(__name__)
@app.route('/')
def Index():
    return render_template("playgrounds.html")

@app.route('/play')
def Play():
    return render_template('playgrounds.html', times=3)

@app.route('/play/<int:times>')
def Play_Level_2(times):
    return render_template('playgrounds.html', times = int(times))

@app.route('/play/<int:times>/<color>')
def Play_Level_3(times, color):
    return render_template('playgrounds.html', times = int(times), color=color)

if __name__=="__main__":
    app.run(debug=True)