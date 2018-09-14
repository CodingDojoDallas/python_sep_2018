from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route('/')
def count():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/addtwo')
def addtwo():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)