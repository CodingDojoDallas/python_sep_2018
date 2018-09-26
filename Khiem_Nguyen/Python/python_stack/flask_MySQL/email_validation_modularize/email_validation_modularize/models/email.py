from flask import Flask , render_template, request, redirect, flash, session
from email_validation_modularize import app
from email_validation_modularize.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = "ThisIsSecret"

class Email:
    def create(self):
        mysql = connectToMySQL("email_validation")
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        data = {
                 'email': request.form['email'],
               }
        result = mysql.query_db(query, data)


        if len(result) != 0:
            flash("This email already exists!")

        if len(request.form["email"]) < 1:
            flash("Email cannot be empty!", "error")

        elif not EMAIL_REGEX.match(request.form["email"]):
            flash("Invalid Email Address!")

        if "_flashes" in session.keys():
            return redirect("/")

        else:
            mysql = connectToMySQL("email_validation")
            query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
            data = {
                 'email': request.form['email'],
                }
            new_email_id = mysql.query_db(query, data)

        return result, new_email_id

    def success(self):
        mysql = connectToMySQL("email_validation")
        all_data = mysql.query_db("SELECT * FROM emails")

        return all_data
