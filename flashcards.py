# from datetime import datetime
from flask import Flask, render_template

from model import db

app = Flask(__name__)
# this calls flask constructor which creates a global Flask application object

# this line makes it a view function , this is a decorator
@app.route("/")
def welcome():
    return render_template("welcome.html",
                           message="Here is a message from the view")

@app.route("/card")
def card_view():
    card = db[3]
    return render_template("card.html",card=card)