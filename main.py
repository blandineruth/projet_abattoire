from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/frame")
def frame():
    return render_template("frame.html")


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/cards")
def cards():
    return render_template("cards.html")

@app.route("/progressbar")
def progressbar():
    return render_template("progressbar.html")

@app.route("/chartjs")
def chartjs():
    return render_template("chartjs.html")

@app.route("/basic")
def basic():
    return render_template("basic.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")


if __name__ == "__main__":
    app.run(debug=True)
