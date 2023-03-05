import os

from flask import (
    Flask,
    jsonify,
    render_template,
    url_for,
    json,
    request
)

import pendulum

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == 'POST':
        start = request.form['start']
        print("start:", start)
        end = request.form['end']
        print("end:", end)
        return render_template("index.html", start=start, end=end)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
