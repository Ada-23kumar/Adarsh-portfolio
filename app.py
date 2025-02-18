from flask import Flask, render_template # type: ignore
from flask_scss import Scss # type: ignore
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)