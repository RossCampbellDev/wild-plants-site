from flask import Blueprint, render_template, request
import datetime

# name of the blueprint, __name__, path to our static folder and templates folder
new_note_blueprint = Blueprint("new_note_blueprint", __name__, static_folder="static", template_folder="templates")


@new_note_blueprint.route("/")
def default():
    datenow = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template("new_note/newnote.html", datenow=datenow)


@new_note_blueprint.route("/submit-new", methods=['POST'])
def form_test():
    new_note = {
        "title":request.form["title-input-text"],
        "date":request.form["date-input-text"],
        "location":request.form["location-input-text"],
        "notes":request.form["notes-input-text"]#,
        #"tags":request.form["tags-input-text"]
    }
    return render_template("new_note/submitnewnote.html", new_note=new_note)

