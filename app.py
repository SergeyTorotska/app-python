from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World, version 1.0.0 !"

