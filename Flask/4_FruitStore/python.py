from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def process_store():
    print(request.form)
    strawberry = request.form["strawberry"]
    rasberry = request.form["rasberry"]
    apple = request.form["apple"]
    name = request.form["name"]
    id_number = request.form["id_number"]
    return render_template("results.html", strawberry=strawberry, rasberry=rasberry, apple=apple, name=name, id_number=id_number)

if __name__== "__main__":
    app.run(debug=True)

