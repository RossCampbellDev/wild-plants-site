from flask import Blueprint, render_template, request, redirect, session
from flasky.user_model import User
import bcrypt


# name of the blueprint, __name__, path to our static folder and templates folder
user_blueprint = Blueprint("user_blueprint", __name__, static_folder="static", template_folder="templates")


# LOGIN
@user_blueprint.route("/", methods=["GET", "POST"])
@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", new_user=True) # TODO: do we need new_user?  can't remember why i put it here
    
    data = request.form
    username = data.get("username-input-text")
    # TODO: check user exists and inform?
    password = data.get("password-input-text")
    if User.check_pass(username, password):
        logged_in_user = User.get_by_username(username)
        if logged_in_user:
            session["user_id"] = str(logged_in_user["_id"])
            session["username"] = username
            session["logged_in"] = True
        return redirect("/review", code=302)
    
    return redirect("/login", code=302)


# LOGOUT
@user_blueprint.route("/logout")
def logout():
    session["user_id"] = None
    session["username"] = None
    session["logged_in"] = False

    return login()


# REGISTER
@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    data = request.form
    username = data.get("username-input-text")
    password = data.get("password-input-text")
    passhash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, passhash=passhash)
    new_user.save()
    return redirect("/login", code=302)