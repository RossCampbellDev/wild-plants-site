from flask import Flask, Blueprint, render_template
app = Flask(__name__)


# BLUEPRINTS
from flasky.new_note_blueprint.new_note_blueprint import new_note_blueprint
from flasky.all_notes_blueprint.all_notes_blueprint import all_notes_blueprint
app.register_blueprint(new_note_blueprint, url_prefix="/")
app.register_blueprint(all_notes_blueprint, url_prefix="/review")


@app.route("/")
def index():
    return render_template("base.html")


def create_app():
    return app