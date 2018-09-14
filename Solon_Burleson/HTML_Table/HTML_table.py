from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
)

@app.route('/')
def Table():
    return render_template("index.html", user_dict = users)



app.run(debug=True)