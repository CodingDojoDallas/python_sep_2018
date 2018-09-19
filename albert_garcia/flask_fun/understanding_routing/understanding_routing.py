from flask import Flask
app = Flask(__name__)  

print(__name__)
@app.route("/")
def HelloWorld():
    return "Hello World!"

@app.route('/dojo')
def Dojo():
    return "Dojo!"

@app.route('/say/<name>')
def Say_Name(name):
    return "Hi "+name

@app.route('/repeat/<amount>/<name>')
def Repeat(amount, name):
    return (name + ' ') * int(amount)

if __name__=="__main__":
    app.run(debug=True)  