from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    all_users = (
   {'first_name' : 'Jihun', 'last_name' : 'Park'},
   {'first_name' : 'Kent', 'last_name' : 'Tse'},
   {'first_name' : 'Kris', 'last_name' : 'Thai'},
   {'first_name' : 'Kobe', 'last_name' : 'Bryant'}
)
    return render_template("index.html", users=all_users)

if __name__ == "__main__":
    app.run(debug=True)