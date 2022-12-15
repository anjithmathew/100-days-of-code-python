from flask import Flask

app = Flask(__name__)



def bold(funcion):
    """ Wrapper function to bold"""
    def wrapper():
        function()
        return wrapper()
@app.route("/")
def world():
    return '<h1 style:"text-align: center">Hello, World!</h1>'\
        '<p> Hello Guyz</p>'\
        '<img src =">'


@app.route("/bye")
def bye():
    return "bye"

@app.route("/<name>")
def greet(name):
    return f"buddy    {na}"

if __name__ =="__main__" :
    app.run(debug=True)
