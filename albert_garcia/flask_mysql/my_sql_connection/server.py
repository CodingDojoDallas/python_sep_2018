from flask import Flask
# import the function connectToMySQL from the file mysqlconnection.pycopy
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('friendships')
# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM users JOIN friendships ON users.id = friendships.friend_1_id;"))
if __name__ == "__main__":
    app.run(debug=True)