from login_and_registration_modularize import app
from flask import Flask, session, render_template, flash, request, redirect
from flask_bcrypt import Bcrypt
from login_and_registration_modularize.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z- ]+$')

bcrypt = Bcrypt(app)
app.secret_key = "ThisIsKey!"

from login_and_registration_modularize.models.login import Login, Register
login = Login()
register = Register()

class Logins:
    def index(self):

        return render_template("index.html")

    def login(self):
        result = login.login()
        return redirect("/success")


    def welcome(self):
        all_users = login.welcome()
        print(all_users,"**************")
        return render_template('success.html', users = all_users)




class Registers:
    def register(self):

        result = register.register()

        return redirect("/success")
