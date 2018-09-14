from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def Form():
    mysql = connectToMySQL("friendsdb")
    friends = mysql.query_db("SELECT * FROM friends")
    print(friends)
    return render_template("index.html", friendsarr = friends)

@app.route('/data', methods=['POST'])
def Data():
    mysql = connectToMySQL("friendsdb")
    fname = request.form['first_name']
    lname = request.form['last_name']
    occ = request.form['occupation']
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
            'first_name': fname,
            'last_name': lname,
            'occupation': occ
            }
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)