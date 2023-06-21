from flask import Blueprint, render_template
from flasky.note_model import Note

# name of the blueprint, __name__, path to our static folder and templates folder
all_notes_blueprint = Blueprint("all_notes_blueprint", __name__, static_folder="static", template_folder="templates")


@all_notes_blueprint.route("/")
def default():
    all_notes = Note.get_all()
    return render_template("allnotes.html", all_notes=all_notes)