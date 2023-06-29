from flask import Flask, Blueprint, render_template
# from flask_bcrypt import Bcrypt
app = Flask(__name__)
# bcrypt = Bcrypt(app)


# BLUEPRINTS
from flasky.new_note_blueprint.new_note_blueprint import new_note_blueprint
from flasky.all_notes_blueprint.all_notes_blueprint import all_notes_blueprint
from flasky.user_blueprint.user_blueprint import user_blueprint
app.register_blueprint(new_note_blueprint, url_prefix="/")
app.register_blueprint(all_notes_blueprint, url_prefix="/review")
app.register_blueprint(user_blueprint, url_prefix="/users")


@app.route("/")
def index():
    return render_template("base.html")


def create_app():
    return app