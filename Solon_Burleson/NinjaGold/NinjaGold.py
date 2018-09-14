from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def Create():
    if 'gold' not in session:
        session['gold'] = 0
    if 'goldnet' not in session:
        session['goldnet'] = 0
    if 'string' not in session:
        session['string'] = ""
    if 'source' not in session:
        session['source'] = ""
    if 'datetime' not in session:
        session['datetime'] = ""
    print(session['goldnet'])
    session['gold'] += int(session['goldnet'])
    if session['goldnet'] > 0:
        session['string'] += "\n"+ "Earned "+ str(session['goldnet'])+" golds from the "+ str(session['source']) + ". " + str(session['datetime'])
    if session['goldnet'] < 0:
        session['string'] += "\n" + "Entered a " + str(session['source']) + " and lost " + str(session['goldnet']*-1) + " golds...Ouch... " + str(session['datetime'])
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def Process():
    x = datetime.datetime.now()
    if int(request.form['source']) == 1:
        session['goldnet'] = random.randrange(10,21)
        session['source'] = "farm"
        session['datetime'] = x.strftime("%x")
        session['datetime'] += " " + str(x.strftime("%X"))
    if int(request.form['source']) == 2:
        session['goldnet'] = random.randrange(5,11)
        session['source'] = "cave"
        session['datetime'] = x.strftime("%x")
        session['datetime'] += " " + str(x.strftime("%X"))
    if int(request.form['source']) == 3:
        session['goldnet'] = random.randrange(2,6)
        session['source'] = "house"
        session['datetime'] = x.strftime("%x")
        session['datetime'] += " " + str(x.strftime("%X"))
    if int(request.form['source']) == 4:
        session['goldnet'] = random.randrange(-50,51)
        session['source'] = "casino"
        session['datetime'] = x.strftime("%x")
        session['datetime'] += " " + str(x.strftime("%X"))
    return redirect('/')

app.run(debug=True)