from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/dojo')
def Dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def Say(name):
    return "Hi " + str(name.capitalize()) 

@app.route('/repeat/<times>/<value>')
def Repeat(times, value):
    return (str(value) + " ") * int(times)


app.run(debug=True)