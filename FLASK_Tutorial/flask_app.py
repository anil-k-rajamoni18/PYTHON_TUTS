from flask import Flask
from flask import escape


app = Flask(__name__) # creation of flask obj  #__main__

@app.route("/")
def hello_world():
    return "<p> Hello, World!  FLASK DEMO</p>"


@app.route("/st")
def hi_student():
    return "<p>HI STUDENT Vemuri Python session SEPTEMBER</p>"

@app.route("/<name>")
def hey(name):
    return f"Hello, {escape(name)}!"




if __name__ == '__main__':
    app.run(debug = True)