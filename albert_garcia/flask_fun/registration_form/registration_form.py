from flask import Flask, render_template, request, redirect, session, flash
import re
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
print(__name__)
@app.route('/')
def Index():
    return render_template('registration_form.html')

@app.route('/register', methods = ['Post'])
def Register():
    # .strftime('%Y-%m-%d')
    now = datetime.today().timestamp()
    print(now)
    email = request.form['email']
    fname = request.form['fname']
    lname = request.form['lname']
    dob = datetime.strptime(request.form['dob'],'%Y-%m-%d').timestamp()
    print(dob)
    print(now - dob)
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    count = 0
    error = 0
    for i in range(0, len(password)):
        if password[i].isupper() == True:
            count += 1
            break

    if len(request.form['email']) == 0:
        flash("Email cannot be blank!", 'email_len')
        error += 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
        error += 1
    if len(request.form['fname']) < 2:
        flash('First name cannot be blank and must be at least 2 characters long!', 'fname_len')
        error += 1
    elif request.form['fname'].isalpha() == False:
        flash('First name can only include letters!', 'fname_alpha')
        error += 1
    if len(request.form['lname']) < 2:
        flash('Last name cannot be blank and must be at least 2 characters long!', 'lname_len')
        error += 1
    elif request.form['lname'].isalpha() == False:
        flash('Last name can only include letters!', 'lname_alpha')
        error += 1
    if len(request.form['password']) < 8 or request.form['password'].isalnum() == False or count < 1:
        flash('Password must be at least 8 characters, contain at least one letter and one number, and at least one uppercase letter!', 'password')
        error += 1
    if request.form['password'] != request.form['confirm_password']:
        flash('Password confirmation did not match', 'match')
        error += 1
    if (now - dob) < 567978991.991719:
        flash('You must be 18 years old to register, please have your parent/guardian register!', 'dob')
        error += 1

    if error < 1:
        flash('Thank you for registering!', 'correct')
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)