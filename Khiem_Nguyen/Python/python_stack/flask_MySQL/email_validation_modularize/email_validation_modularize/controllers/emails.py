from flask import Flask , render_template, redirect





from email_validation_modularize.models.email import Email
email = Email()

class Emails:
    def index(self):

        return render_template("index.html")

    def create(self):
        result = email.create()
        new_email_id = email.create()
        return redirect('/success')

    def success(self):
        all_data = email.success()

        return render_template('success.html', emails = all_data)
