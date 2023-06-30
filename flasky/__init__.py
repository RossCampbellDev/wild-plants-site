from flask import Flask, Blueprint, redirect, session
from functools import wraps
from flasky.user_model import User

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


# check login decorator
def logged_in(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect("/users", code=302)
        
        return func(*args, **kwargs)

    return decorated_view


# BLUEPRINTS
from flasky.new_note_blueprint.new_note_blueprint import new_note_blueprint
from flasky.all_notes_blueprint.all_notes_blueprint import all_notes_blueprint
from flasky.user_blueprint.user_blueprint import user_blueprint
app.register_blueprint(new_note_blueprint, url_prefix="/new")
app.register_blueprint(all_notes_blueprint, url_prefix="/review")
app.register_blueprint(user_blueprint, url_prefix="/users")


@app.route("/")
def index():
    return redirect("/users", code=302)


def create_app():
    return app