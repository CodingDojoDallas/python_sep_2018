from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
	if 'visits' in session:
		session['visits'] += 1
	else:
		session['visits'] = 1
	return render_template('index.html', visits=session['visits'])
if __name__=="__main__":
	app.run(debug=True)