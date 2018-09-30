

from email_validation_modularize import app
from email_validation_modularize.controllers.emails import Emails

emails = Emails()

@app.route("/")
def index():

    return emails.index()

@app.route("/validation", methods=['POST'])
def create():

    return emails.create()

@app.route('/success')
def success():

    return emails.success()
