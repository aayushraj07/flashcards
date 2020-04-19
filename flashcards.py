from flask import Flask

app = Flask(__name__)
#this calls flask constructor which creates a global Flask application object

@app.route("/")
#this line makes it a view function , this is a decorator

def welcome():
    return "Welcome to my Flash Cards application"