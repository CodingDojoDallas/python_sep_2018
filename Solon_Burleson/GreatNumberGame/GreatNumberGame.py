from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def numberGame():
    if 'num' not in session:
        session['num'] = random.randrange(1, 101)
    print(session['num'])
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def Check():
    session['guess'] = request.form['guess']
    if int(session['guess']) == int(session['num']):
        session['result'] = "equal"
    if int(session['guess']) > int(session['num']):
        session['result'] = "high"
    if int(session['guess']) < int(session['num']):
        session['result'] = "low"
    return redirect('/')

@app.route('/clear')
def Clear():
    session.pop('num')
    session.pop('result')
    session.pop('guess')
    return redirect('/')


app.run(debug=True)