from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key ='thisIsSecret'

print(__name__)
@app.route('/')
def Index():
    rand = random.randrange(1,101)
    print(rand)
    return render_template('number_game.html', rand = session['rand'])

@app.route('/guess', methods = ['POST'])
def Guess():
    guess = request.form['guess']
    if int(guess) < rand:
        return render_template('too_low.html')
    if int(guess) > rand:
        return render_template('too_high.html')
    if int(guess) == rand:
        return render_template('play_again.html')
@app.route('/new', methods = ['POST'])
def New():
    rand = random.randrange(1,101)
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)