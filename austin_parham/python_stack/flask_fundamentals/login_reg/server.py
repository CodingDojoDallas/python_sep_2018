from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    if 'reroute' not in session:    
        session['reroute'] = ""
    mysql = connectToMySQL("emails")
    emails = mysql.query_db("SELECT * FROM emails")
    print("Current reroute status is", session['reroute'])
    return render_template('index.html', emails=emails)

@app.route('/register', methods=['post'])
def verify():
    mysql = connectToMySQL("emails")
    emails = mysql.query_db("SELECT * FROM emails")

    for user in emails:
        if user['email_address'] == request.form['reg_email']:
            flash("Email has been taken!")
            session['reroute'] = "register"
            return redirect('/')

    if len(request.form['first_name']) < 2:
        flash("First name must be at least two characters long!")
        session['reroute'] = "register"
        print( "Current reroute attempt is",session['reroute'])
        return redirect('/')
    if not NAME_REGEX.match(request.form['first_name']):
        flash("First name can only contain letters.")
        session['reroute'] = "register"
        return redirect('/')

    if len(request.form['last_name']) < 2: #Last Name
        flash("Last name must be at least two characters long!")
        session['reroute'] = "register"
        return redirect('/')
    if not NAME_REGEX.match(request.form['last_name']):
        flash("Last name can only contain letters.")
        session['reroute'] = "register"
        return redirect('/')

    if len(request.form['reg_password']) < 8: #Password
        flash("Password must be at least 8 characters long!")
        session['reroute'] = "register"
        return redirect('/')

    if request.form['reg_password'] != request.form['confirm_password']:
        flash("Passwords do not match.")
        session['reroute'] = "register"
        return redirect('/')

    session['reg_email'] = request.form['reg_email']
    session['password'] = request.form['reg_password']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    return redirect('/insert')

@app.route('/insert')
def insert():
    mysql = connectToMySQL("emails")
    query = "INSERT INTO emails (email_address, password, first_name, last_name) VALUES (%(email)s, %(password)s, %(first_name)s, %(last_name)s);"
    data = {
             'email': session['reg_email'],
             'password': session['password'],
             'first_name': session['first_name'],
             'last_name': session['last_name']
           }
    new_email = mysql.query_db(query, data)
    session['email'] = session['reg_email']
    print("A new user has been added!",session['reg_email'])
    return redirect('/login')

@app.route('/ver_login', methods=['post'])
def ver_login():
    mysql = connectToMySQL("emails")
    emails = mysql.query_db("SELECT * FROM emails")

    if len(request.form['email']) < 1:
        flash("Please input email address")
        session['reroute'] = "login"
        return redirect('/')

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Must be valid email address.")

    for user in emails:
        if user['email_address'] == request.form['email']:
            print("MATCH!",user['email_address'],"is equal to",request.form['email'])
            if user['password'] == request.form['login_password']:
                session['email'] = request.form['email']
                print(session['email'])
                return redirect('/login')
            else:
                flash("Invalid password.")
                session['reroute'] = "login"
                return redirect('/')
        else:
            print(user['email_address'],"does not equal",request.form['email'])
    flash("Invalid username/password.")
    print("List of users", emails)
    session['reroute'] = "login"
    return redirect('/')

@app.route('/login')
def success():
    mysql = connectToMySQL("emails")
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template('login.html', emails=emails)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)