from flask import Flask, redirect, render_template, flash, session, request

from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z- ]+$')
app = Flask(__name__)

app.secret_key = "ThisIsKey!"


@app.route("/")
def index():

    return redirect("/users")


@app.route("/users")
def users():
    mysql = connectToMySQL('user_assignment')
    all_users = mysql.query_db("SELECT * FROM users")

    return render_template("users.html", all_users = all_users)

@app.route("/users/new")
def new_users():

    return render_template("new_users.html")

@app.route("/users/create", methods=["POST"])
def create_users():

    if len(request.form["first_name"]) < 1:
        flash("first name required", "first_name")
    elif len(request.form["first_name"]) < 3:
        flash("first name needs to be at least 2 letters", "first_name")
    elif not NAME_REGEX.match(request.form["first_name"]):
        flash("first name cannot have numbers!", "first_name")
    else:
        session["first_name"] = request.form["first_name"]

    if len(request.form["last_name"]) < 1:
        flash("last name required", "last_name")
    elif len(request.form["last_name"]) < 3:
        flash("last name needs to be at least 2 letters", "last_name")
    elif not NAME_REGEX.match(request.form["last_name"]):
        flash("last name cannot have numbers!", "last_name")
    else:
        session["last_name"] = request.form["last_name"]

    mysql = connectToMySQL('user_assignment')
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
             'email': request.form['email'],
           }
    result = mysql.query_db(query, data)

    if len(request.form["email"]) < 1:
        flash("email required", "email")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("You must input a valid email address!", "email")
    elif len(result) != 0:
        flash("This email already exists!", "email")
    else:
        session["email"] = request.form["email"]


    if '_flashes' in session.keys():
        return redirect("/users/new")

    else:
        session['logged_in'] = True
        mysql = connectToMySQL('user_assignment')
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name': request.form['last_name'],
                 'email': request.form['email'],
               }
        mysql.query_db(query, data)

    return redirect("/users")

@app.route("/users/<x>")
def show_info(x):

    if "id" not in session:
        session["id"] = 0
    session["id"] = x
    print(session["id"])
    mysql = connectToMySQL('user_assignment')
    this_user = mysql.query_db("SELECT * FROM users where id={}".format(x))


    return render_template("this_user.html", this_user = this_user)

@app.route("/users/<y>/destroy")
def destroy(y):

    if "id" not in session:
        session["id"] = y
    print(session["id"])

    mysql = connectToMySQL('user_assignment')
    this_user = mysql.query_db("DELETE FROM users where id={}".format(y))

    return redirect ("/users")

@app.route("/users/<z>/edit")
def update(z):

    mysql = connectToMySQL('user_assignment')
    this_user = mysql.query_db("SELECT * FROM users where id={}".format(z))

    if "id" not in session:
        session["id"] = this_user[0]["id"]
    else: session["id"] = this_user[0]["id"]
    if "first_name" not in session:
        session["first_name"] = this_user[0]["first_name"]
    else:
         session["first_name"] = this_user[0]["first_name"]
    if "last_name" not in session:
        session["last_name"] = this_user[0]["last_name"]
    else: session["last_name"] = this_user[0]["last_name"]
    if "email" not in session:
        session["email"] = this_user[0]["email"]
    else: session["email"] = this_user[0]["email"]

    return render_template("/update.html")

@app.route("/users/process_update",  methods=["POST"])
def process_update():


    mysql = connectToMySQL('user_assignment')
    query = "UPDATE users SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s where id={}".format(session["id"])
    data = {
             'first_name': request.form["first_name"],
             'last_name': request.form["last_name"],
             'email': request.form["email"],
           }
    mysql.query_db(query, data)




    return redirect("/users")




    if __name__ == "__main__":
        app.run(debug=True)
