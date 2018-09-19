# classes
from flask import redirect, render_template
from mvc import app
from mvc.config import routes
from mvc.models.friend import 
class Friends:
    def Index(self):
        all_friends = friend.Index()
        return render_template('c_r_friends.html', friends = all_friends, length = length)

class Add:
    def Add(self):
        new_friend_id = friend.Add()
        return redirect('/')