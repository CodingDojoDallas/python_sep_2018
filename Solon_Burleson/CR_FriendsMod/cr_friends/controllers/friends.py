from flask import render_template, redirect
from cr_friends.models.friends import Friend

friend = Friend()

class Friends:
    def Form(self):
        friends = friend.Form()
        return render_template("index.html", friendsarr = friends)

    def Data(self):
        result = friend.Data()
        return redirect('/')