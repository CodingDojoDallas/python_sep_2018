from cr_friends.config.mysqlconnection import connectToMySQL
from flask import render_template, request, redirect
from cr_friends.models.friend import Friend
friend = Friend()

class Friends:
    def index(self):
        all_friends = friend.index()
        return render_template('index.html', friends = all_friends)

    def create(self):
        new_friend_id = friend.create()
        return redirect('/')
