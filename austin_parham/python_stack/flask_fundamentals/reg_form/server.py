from flask import Flask, render_template, request, redirect, session, flash
import re
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def home_input():
	return render_template("index.html")
@app.route('/process', methods=['post'])
def process():
	if len(request.form['email']) < 1: #Email
		flash(u"Email cannot be empty!",'error')
		return redirect('/')

	if len(request.form['first_name']) < 1: #First Name
		flash("First name cannot be empty!")
		return redirect('/')
	if not NAME_REGEX.match(request.form['first_name']):
		flash("First name can only contain letters.")
		return redirect('/')

	if len(request.form['last_name']) < 1: #Last Name
		flash("Last name cannot be empty!")
		return redirect('/')
	if not NAME_REGEX.match(request.form['last_name']):
		flash("Last name can only contain letters.")
		return redirect('/')

	if len(request.form['password']) < 1: #Password
		flash("Password cannot be empty")
		return redirect('/')

	if len(request.form['confirm_password']) < 1: #Current Password
		flash("Please confirm your new password.")
		return redirect('/')
	if request.form['password'] != request.form['confirm_password']:
		flash("Passwords do not match.")
		return redirect('/')
if __name__=="__main__":
	app.run(debug=True)