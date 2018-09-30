from flask import Flask
from login_and_registration_modularize import app
from login_and_registration_modularize.controllers.logins import Logins, Registers

from login_and_registration_modularize.config.mysqlconnection import connectToMySQL

logins = Logins()
registers = Registers()

@app.route("/")
def index():

    return logins.index()


@app.route("/register", methods=["POST"])
def register():

    return registers.register()


@app.route("/login", methods=["POST"])
def login():

    return logins.login()

@app.route("/success")
def welcome():

    return logins.welcome()
