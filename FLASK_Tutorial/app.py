from flask import Flask , render_template ,escape



app = Flask(__name__)



mv = [
    {
    "name" : "Intersellar",
    "genre" : "Scifi",
    "y " : "2001"
    },
    {
    "name" : "Dont breathe ",
    "genre" : "Thriller",
    "y " : "2021"
    }
]

some_list = [10,303,404,21,202,30]


person={
    "name" :"AkRajamoni",
    "class":"python",
    "fee":10000
}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/h2")
def h1():
    return "<h1>Hey HI from Flask </h1>"

# @app.route('/home')
# def  home():
#     return render_template('home.html',movies = mv  , title = "MOVIES PAGE")


@app.route('/about')
def about():
    return render_template('about.html',list_data = some_list)


@app.route("/demo")
def demo():
    return render_template("demo.html",senddata = person)


@app.route("/<nm>")
def hey(nm):
    return f"Hello, {escape(nm)}!"

if __name__ == '__main__':
    app.run(debug=True)
