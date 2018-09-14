from flask import Flask, render_template, request, redirect, session, flash
# import the function connectToMySQL from the file mysqlconnection.pycopy
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def Index():
    mysql = connectToMySQL("friendsdb")
    all_friends = mysql.query_db("SELECT * FROM friends")
    length = len(all_friends)
    print("Fetched all friends", all_friends)
    return render_template('c_r_friends.html', friends = all_friends, length = length)

@app.route('/add', methods = ['POST'])
def Add():
    error = 0
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
    if len(request.form['occupation']) < 2:
        flash('Occupation cannot be blank if none state none', 'occupation_len')
        error += 1
    elif request.form['occupation'].isalpha() == False:
        flash('Occupation can only include letters!', 'occupation_alpha')
        error += 1
    if error < 1:
        mysql = connectToMySQL("friendsdb")
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'occupation' : request.form['occupation']
        }
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
        new_friend_id =mysql.query_db(query, data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)








