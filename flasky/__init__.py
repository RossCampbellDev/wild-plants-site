# FLASK
from flask import Flask, Blueprint, render_template, url_for
app = Flask(__name__)


import os
from dotenv import load_dotenv
load_dotenv()


# LOAD ENV VARS
app.secret_key = os.environ.get('SECRET_KEY')
DB_URL = os.environ.get('DB_URL')


# BLUEPRINTS
from new_note_blueprint.new_note_blueprint import new_note_blueprint
from all_notes_blueprint.all_notes_blueprint import all_notes_blueprint
app.register_blueprint(new_note_blueprint, url_prefix="/")
app.register_blueprint(all_notes_blueprint, url_prefix="/review")


@app.route("/")
def index():
    return render_template("base.html")


app.run(host="0.0.0.0", port=31337, debug=True)