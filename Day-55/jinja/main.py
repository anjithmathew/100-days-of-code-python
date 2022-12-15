from flask import Flask, render_template
import random
import datetime as dt
import requests


app = Flask(__name__)


@app.route('/')
def home():
    year_now = dt.datetime.now().year
    random_number = random.randint(1,10)
    return render_template("index.html",x= random_number,y=year_now)


@app.route("/blog")

def blog():
    data = requests.get("https://www.npoint.io/docs/c790b4d5cab58020d391").json()
    render_template("blog.html",posts=data)

if __name__ == "__main__":
    app.run(debug=True)


