from flask import Flask, render_template, request, redirect, flash
import re
app = Flask(__name__)
app.secret_key="shdjfklahsdf"

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')

@app.route('/')
def Form():
    return render_template("index.html")

@app.route('/valid', methods=['POST'])
def Valid():
    if len(request.form['first_name']) < 1:
        flash(u'*First Name was not entered.', 'fname')
    if len(request.form['last_name']) < 1:
        flash(u'*Last Name was not entered.', 'lname')
    if len(request.form['password']) < 8:
        flash(u'*Password must be atleast 8 characters.', 'password')
    elif re.search('[0-9]', request.form['password']) is None:
        flash(u'*Must contain a number.', 'pw_num')
    elif re.search('[A-Z]', request.form['password']) is None:
        flash(u'*Must contain a capital.', 'pw_cap')
    if request.form['confirm_pass'] != request.form['password']:
        flash(u'*Passwords do not match.', 'confirm_pass')
    if len(request.form['email']) < 1:
        flash(u'*Email not entered.', 'noemail')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'*Email not valid.', 'email_invalid')
    else:
        flash(u'Thanks for submitting your information', 'correct')

    return redirect('/')

    

app.run(debug=True)