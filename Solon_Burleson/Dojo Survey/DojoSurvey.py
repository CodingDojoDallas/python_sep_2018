from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def create_user():
    return render_template("form.html")

@app.route('/user', methods = ["POST"])
def user():
    print('name', request.form['name'])
    print('location', request.form['location'])
    print('language', request.form['language'])
    print('comment', request.form['comment'])
    if len(request.form['name']) > 0 and len(request.form['comment']) > 0 and len(request.form['comment']) < 121:
        return render_template("user.html")
    else:
        flash('Validation error check name and comments')
        return redirect('/')
    
@app.route('/danger')
def danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')

app.run(debug=True)