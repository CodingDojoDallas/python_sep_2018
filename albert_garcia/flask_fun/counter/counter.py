from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key ='thisIsSecret'

print(__name__)
@app.route('/')
def Index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    print(session['count'])
    return render_template('counter.html', count = session['count'])

@app.route('/counter')
def Add_Twp():
    session['count'] += 1
    return redirect('/')

@app.route('/clear')
def Clear():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)