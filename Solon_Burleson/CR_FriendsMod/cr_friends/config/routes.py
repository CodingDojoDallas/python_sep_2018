from cr_friends.controllers.friends import Friends
from cr_friends import app

friends = Friends()

@app.route('/')
def Form():
    return friends.Form()

@app.route('/data', methods=['POST'])
def Data():
    return friends.Data()