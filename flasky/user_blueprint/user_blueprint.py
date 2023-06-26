from flask import Blueprint, render_template, request
from flasky.user_model import User


# name of the blueprint, __name__, path to our static folder and templates folder
user_blueprint = Blueprint("user_blueprint", __name__, static_folder="static", template_folder="templates")


@user_blueprint.route("/")
def login():
    return render_template("login.html")


@user_blueprint.route("/register")
def register():
    return render_template("register.html")