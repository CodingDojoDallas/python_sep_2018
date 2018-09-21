from flask import request
from cr_friends.config.mysqlconnection import connectToMySQL

class Friend():
    def Form(self):
        mysql = connectToMySQL("friendsdb")
        friends = mysql.query_db("SELECT * FROM friends")
        return friends
    
    def Data(self):
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
        return new_friend_id
