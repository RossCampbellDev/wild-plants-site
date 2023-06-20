# FLASK
from flask import Flask, Blueprint, render_template, url_for
app = Flask(__name__)


import os
from dotenv import load_dotenv
load_dotenv()


# LOAD ENV VARS
# app.secret_key = os.environ.get('SECRET_KEY')
MONGO_CONN_STRING = os.environ.get('MONGO_CONN_STRING')


# MONGO
import pymongo
from pymongo import MongoClient
client = MongoClient(MONGO_CONN_STRING)
db = client["wild-plants"]
wild_plants_collection = db["wild-plants-collection"]
app.config["all_notes"] = wild_plants_collection.find()


# BLUEPRINTS
from new_note_blueprint.new_note_blueprint import new_note_blueprint
from all_notes_blueprint.all_notes_blueprint import all_notes_blueprint
app.register_blueprint(new_note_blueprint, url_prefix="/")
app.register_blueprint(all_notes_blueprint, url_prefix="/review")


@app.route("/")
def index():
    return render_template("base.html")


app.run(host="0.0.0.0", port=31337, debug=True)