from flask import Flask, session, render_template, flash, request, redirect
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z- ]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "ThisIsKey!"



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

#validate first_name
    if len(request.form["first_name"]) < 1:
        flash("first name required", "first_name")
    elif len(request.form["first_name"]) < 3:
        flash("first name needs to be at least 2 letters", "first_name")
    elif not NAME_REGEX.match(request.form["first_name"]):
        flash("first name cannot have numbers!", "first_name")
    else:
        session["first_name"] = request.form["first_name"]

#validate last_name
    if len(request.form["last_name"]) < 1:
        flash("last name required", "last_name")
    elif len(request.form["last_name"]) < 3:
        flash("last name needs to be at least 2 letters", "last_name")
    elif not NAME_REGEX.match(request.form["last_name"]):
        flash("last name cannot have numbers!", "last_name")
    else:
        session["last_name"] = request.form["last_name"]
#validate email

    mysql = connectToMySQL('simple_wall_db')
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


#validate password
    if len(request.form["password"]) < 1:
        flash("password required", "password")
    elif len(request.form["password"]) < 8 :
        flash("password needs to be at least 8 characters", "password")
#validate confirm_password
    if len(request.form["confirm_password"]) < 1:
        flash("confirm password required", "confirm_password")
    elif request.form["password"] != request.form["confirm_password"]:
        flash("password do not match!", "confirm_password")
    else:
        session["password"] = request.form["password"]

    if '_flashes' in session.keys():
        return redirect("/")
#encryting_password
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        session['email'] = request.form['email']
        session['logged_in'] = True
        mysql = connectToMySQL('simple_wall_db')
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pass_hash)s, NOW(), NOW());"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name': request.form['last_name'],
                 'email': request.form['email'],
                 'pass_hash': pw_hash
               }
        mysql.query_db(query, data)
        flash("You have successfully registered! Please log in now!", "status")
        return redirect("/")

    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    mysql = connectToMySQL('simple_wall_db')
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
             'email': request.form['email'],
           }
    result = mysql.query_db(query, data)

    if len(request.form['email']) < 1:
        flash("Email required", "login_status")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("You must input a valid email address!", "login_status")

    if len(request.form['password']) < 1:
        flash("Password required", "login_status")

    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['email'] = request.form['email']
            session['logged_in'] = True
            session["id"] = result[0]["id"]
            session["first_name"] = result[0]["first_name"]
            print(session["id"])

            return redirect('/wall')

    flash("Could not login", "login_status")
    return redirect('/')


@app.route("/wall")
def welcome():
    if session['logged_in'] == False:
        flash("Please Log in", "status")
        return redirect('/')

    elif 'email' not in session:
        flash("Please Log in", "status")
        return redirect('/')

    else:

        unique_session_id = session["id"]
        mysql = connectToMySQL("simple_wall_db")
        number_of_messages=mysql.query_db("Select COUNT(recipient_id) from messages where recipient_id={}".format(unique_session_id))

        unique_session_id = session["id"]
        mysql = connectToMySQL("simple_wall_db")
        user_messages=mysql.query_db("SELECT * from messages where recipient_id ={}".format(unique_session_id))

        unique_session_id = session["id"]
        mysql = connectToMySQL("simple_wall_db")
        receivers=mysql.query_db("SELECT * from users where id !={}".format(unique_session_id))

        unique_session_id = session["id"]
        mysql = connectToMySQL("simple_wall_db")
        senders_name=mysql.query_db("select users.first_name, messages.sender_id, users.id, messages.message, messages.created_at, messages.recipient_id from messages join users on users.id = messages.sender_id where recipient_id ={}".format(unique_session_id))



        return render_template('wall.html', number_of_messages = number_of_messages, user_messages = user_messages, receivers = receivers, senders_name = senders_name )

@app.route("/send/<x>", methods=["POST"])
def post(x):


    mysql = connectToMySQL("simple_wall_db")
    query = "INSERT INTO messages ( message, sender_id, recipient_id, created_at, updated_at) VALUES (%(message)s, %(sender_id)s, %(recipient_id)s, NOW(), NOW());"
    data = {
             'message': request.form['message'],
             'sender_id': session["id"],
             'recipient_id' : x ,

           }
    message_sent=mysql.query_db(query, data)


    return redirect('/wall')





if __name__ == '__main__':
    app.run(debug=True)
