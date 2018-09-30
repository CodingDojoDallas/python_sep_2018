from flask import Flask , render_template, request, redirect, flash, session
# import the function connectToMySQL from the file mysqlconnection.py
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = connectToMySQL("email_validation")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validation", methods=['POST'])
def create():
    mysql = connectToMySQL("email_validation")
    query = "SELECT * FROM emails WHERE email = %(email)s;"
    data = {
             'email': request.form['email'],
           }
    result = mysql.query_db(query, data)


    if len(result) != 0:
        flash("This email already exists!")

    if len(request.form["email"]) < 1:
        flash("Email cannot be empty!", "error")

    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email Address!")

    if "_flashes" in session.keys():
        return redirect("/")

    else:
        mysql = connectToMySQL("email_validation")
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        data = {
             'email': request.form['email'],
            }
        new_email_id = mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def success():
    mysql = connectToMySQL("email_validation")
    all_data = mysql.query_db("SELECT * FROM emails")
    print("Fetched all data", all_data)
    return render_template('success.html', emails = all_data)


# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM email;"))
if __name__ == "__main__":
    app.run(debug=True)
