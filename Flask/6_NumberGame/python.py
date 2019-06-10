from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key = 'secret'

@app.route('/')
def index():
    if session.has_key('correct_number') == False:
        session['correct_number'] = random.randrange(0,101)
    return render_template("index.html")

@app.route('/guesses', methods=['POST'])
def return_answer():
    guess = request.form['guess']
    if not len(guess) > 0:
        return redirect("/")

    elif int(guess) > session['correct_number']:
        session['guess_status'] = 'high'
        return redirect("/")
    elif int(guess) < session['correct_number']:
        session['guess_status'] = 'low'
        return redirect("/")
    elif int(guess) == session['correct_number']:
        session['guess_status'] = 'right'
        session.pop('correct_number')
        return redirect("/")
    else: 
        print ' please enter a number btw 0 - 101 '
        return redirect("/")

@app.route('/reload')
def reload():
    session['guess_status'] = 'hide_div'
    return redirect('/')

app.run(debug=True)