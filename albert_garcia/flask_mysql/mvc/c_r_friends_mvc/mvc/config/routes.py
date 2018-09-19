# routes
from mvc import app
from mvc.controllers.friends import Friends
from mvc.controllers.friends import Add
friends = Friends()
add = Add()
@app.route('/')
def Index():
    return friends.Index()

@app.route('/add', methods = ['POST'])
def Add():
    return friends.Add()