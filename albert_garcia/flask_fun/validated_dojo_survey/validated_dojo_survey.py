from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)  
app.secret_key = 'KeepItSecretKeepItSafe'

print(__name__)
@app.route("/")
def Index():
    return render_template('val_dojo_survey.html')

@app.route("/results", methods =['POST'])
def Results():
    if len(request.form['name']) < 2:
        flash("Name must be 2+ characters!", 'name')
    if len(request.form['comment']) < 4 or len(request.form['comment']) > 120:
        flash("Comment must be between 4 and 120 characters!", 'comment')
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return render_template('val_dojo_survey_results.html')

@app.route('/home', methods = ['POST'])
def Home():
    return redirect('/')

@app.route('/danger')
def Danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)