from flask import Flask, render_template, request, redirect, session, flash
# import the function connectToMySQL from the file mysqlconnection.pycopy
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/validate', methods = ['POST'])
def Add():
    error = 0
    mysql = connectToMySQL("email_validation")
    elist = mysql.query_db("select * from emails;")
    print("Fetched all emails", elist)
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
        error += 1
        return redirect('/')
    else:
        for i in elist:
            if i['address'] == request.form['email']:
                flash("Email address has already been added", 'check')
                error += 1
                return redirect('/')
    if error < 1:
        session['email'] = request.form['email']
        return redirect('/create')
@app.route('/create')
def create():
    mysql = connectToMySQL("email_validation")
    query = "insert into emails (address, created_at, updated_at) values (%(email)s, now(), now());"
    data = {
        'email' : session['email']
    }
    new_email_id =mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def success():
    mysql = connectToMySQL("email_validation")
    elist = mysql.query_db("select * from emails;")
    print("Fetched all emails", elist)
    return render_template('validate.html', elist = elist)

if __name__ == "__main__":
    app.run(debug=True)








