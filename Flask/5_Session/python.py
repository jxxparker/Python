from flask import Flask, render_template,request,redirect, session

app = Flask(__name__)
app.secret_key = "secret"
app.count = 0

@app.route("/")
def index():
    if session.has_key('counters') == False:
        session['counters'] = 1
    else:
        session['counters'] += 1
    return render_template("index.html", count=session['counters'])

@app.route("/increment", methods=['POST'])
def add_two():
    session['counters'] += 1
    return redirect("/")

@app.route("/reset", methods=['POST'])
def reset():
    session['counters'] = 0
    return redirect("/")

app.run(debug=True)