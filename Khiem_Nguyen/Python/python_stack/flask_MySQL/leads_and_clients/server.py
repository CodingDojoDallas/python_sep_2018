from flask import Flask , render_template, request, redirect
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL("leads_and_clients")
@app.route('/')
def index():
    mysql = connectToMySQL("leads_and_clients")
    all_data = mysql.query_db("SELECT * FROM data")
    print("Fetched all data", all_data)
    return render_template('index.html', data = all_data)

@app.route('/create_friend', methods=['POST'])
def create():
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')
# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM friends;"))
if __name__ == "__main__":
    app.run(debug=True)
