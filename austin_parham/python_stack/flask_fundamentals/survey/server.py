from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def home_input():
	return render_template("index.html")

@app.route('/process', methods=['post'])
def process():
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		return redirect('/')
	if len(request.form['comment']) < 1:
		flash("Comments cannot be empty!")
		return redirect('/')
	if len(request.form['comment']) > 120:
		flash("Comments cannot exceed 120 characters!")
		return redirect('/')
	else:
		name = request.form['name']
		location = request.form['location']
		language = request.form['language']
		comment = request.form['comment']
		return render_template("results.html", name=name, location=location, comment=comment, language=language)
	
if __name__=="__main__":
	app.run(debug=True)