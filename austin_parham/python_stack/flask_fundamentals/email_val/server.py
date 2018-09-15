from flask import Flask, render_template, request, redirect, session, flash
import re

from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    mysql = connectToMySQL("emails")
    emails = mysql.query_db("SELECT * FROM emails")
    print("Fetched all customers", emails)
    return render_template('index.html', emails=emails)

@app.route('/verify', methods=['post'])
def verify():
    mysql = connectToMySQL("emails")
    emails = mysql.query_db("SELECT * FROM emails")
    for email in emails:
        if email['email_address'] == request.form['email']:
            flash("Email has been taken!")
            return redirect('/')
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!")
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Must be valid Email address!")
        return redirect('/')
    else:
        session['email'] = request.form['email']
        return redirect('/insert')

@app.route('/insert')
def insert():
    mysql = connectToMySQL("emails")
    query = "INSERT INTO emails (email_address) VALUES (%(email)s);"
    data = {
             'email': session['email']
           }
    new_email = mysql.query_db(query, data)
    return redirect('/success')
    
@app.route('/success')
def success():
    mysql = connectToMySQL("emails")
    emails = mysql.query_db("SELECT * FROM emails")
    print("Fetched all customers", emails)
    return render_template('results.html', emails=emails)

if __name__ == "__main__":
    app.run(debug=True)