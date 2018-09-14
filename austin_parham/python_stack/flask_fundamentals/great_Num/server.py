from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
	if 'answer' not in session:
		session['answer']= int(random.randrange(0, 101))
	print('The answer is',session['answer'])
	return render_template('index.html')
@app.route('/result', methods=['post'])
def result():
	session['guess'] = int(request.form['guess'])
	print('The guess is logged as',session['guess'])

	return redirect('/')
@app.route('/reset')
def reset():
	session.clear()

	return redirect('/')
if __name__=="__main__":
	app.run(debug=True)