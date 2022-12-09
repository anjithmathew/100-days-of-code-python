from flask import Flask

app = Flask(__name__)

@app.route("/")
def world():
    return "<p>Hello, World!</p>"