from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World, version 2.0.0 !"
