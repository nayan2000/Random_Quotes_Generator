from flask import Flask 
app = Flask(__name__)

@app.route("/")
def index():
    return "You're on the index page"

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
    app.run()