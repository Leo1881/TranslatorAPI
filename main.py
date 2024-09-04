from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>/")
def api(word):
    definition = word.upper()
    result_dictionary = {"word": word, "definition": definition}
    return result_dictionary


app.run(debug=True)