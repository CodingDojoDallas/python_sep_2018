from flask import Flask, render_template, redirect, request, session, flash
import re
from datetime import datetime
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
app = Flask(__name__)
bcrypt = Bcrypt(app) 
app.secret_key = 'its a secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def Index():
    if session['logout'] == 1:
        flash('You have been logged out', 'logout')
        session['logout'] += 1
    return render_template('index.html')
    
@app.route('/register', methods = ['POST'])
def register():
    error = 0
    now2 = datetime.today()
    print(now2)
    now = datetime.today().timestamp()
    print(now)
    session['fname'] = request.form['first_name']
    session['lname'] = request.form['last_name']
    if len(request.form['dob']) < 1:
        flash('Date of birth connot be blank', 'blank_dob') 
        error += 1
    elif len(request.form['dob']) > 1: 
        dob = datetime.strptime(request.form['dob'],'%Y-%m-%d').timestamp()
        print(dob)
        print(now - dob)
        if (now - dob) < 567978991.991719:
            flash('You must be 18 years old to register, please have your parent/guardian register!', 'dob')
            error += 1
    password_attempt = request.form['password']

    count = 0
    for i in range(0, len(password_attempt)):
        if password_attempt[i].isupper() == True:
            count += 1
            break

    if len(request.form['email']) == 0:
        flash("Email cannot be blank!", 'email_len')
        error += 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
        error += 1
    if len(request.form['first_name']) < 2:
        flash('First name cannot be blank and must be at least 2 characters long!', 'fname_len')
        error += 1
    elif request.form['first_name'].isalpha() == False:
        flash('First name can only include letters!', 'fname_alpha')
        error += 1
    if len(request.form['last_name']) < 2:
        flash('Last name cannot be blank and must be at least 2 characters long!', 'lname_len')
        error += 1
    elif request.form['last_name'].isalpha() == False:
        flash('Last name can only include letters!', 'lname_alpha')
        error += 1
    if len(request.form['password']) < 8 or request.form['password'].isalnum() == False or count < 1:
        flash('Password must be at least 8 characters, contain at least one letter and one number, and at least one uppercase letter!', 'password')
        error += 1
    if request.form['password'] != request.form['confirm_password']:
        flash('Password confirmation did not match', 'match')
        error += 1
    mysql = connectToMySQL("login_register")
    elist = mysql.query_db("select email from users;")
    print("Fetched all emails", elist)
    for i in elist:
        if i['email'] == request.form['email']:
            flash("Email address has already been registered", 'reg_check')
            error += 1
            return redirect('/')
    if error == 0:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL("login_register")
        query = "insert into users (first_name, last_name, email, password, dob, created_at, updated_at) values (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, %(dob)s, now(), now());"
        data = {
        'email' : request.form['email'],
        'pw_hash' : pw_hash,
        'first_name' : session['fname'],
        'last_name' : session['lname'],
        'dob' : request.form['dob']
        }
        new_user_id =mysql.query_db(query, data)
        print(new_user_id)
        session['reg'] = 1
        return redirect('/success')

@app.route('/success')
def reg_success():
    if session['reg'] == 1:
        flash('Thank you for registering', 'registered')
        session['reg'] += 1
    return render_template('success.html')

@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    session['logout'] = 1
    return redirect('/')


@app.route('/login', methods = ['POST'])
def login():
    password = request.form['lpassword']
    error = 0
    mysql = connectToMySQL("login_register")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
            'email': request.form['email']
        }
    elist = mysql.query_db(query, data)
    print("Fetched all emails", elist)
    if len(elist) < 1:
        flash("Email or password does not match our records!", 'login_error')
        return redirect('/')
    if bcrypt.check_password_hash(elist[0]['password'], password):
        session['fname'] = elist[0]['first_name']
        session['id'] = elist[0]['id']
        session['status'] = "logged_in"
        session['reg'] = 0
        return redirect('/success')
    else:
        flash("Email or password does not match our records!", 'login_error')
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)