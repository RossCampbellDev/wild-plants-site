from flask import Blueprint, render_template, request, current_app
from flasky import wild_plants_collection

# name of the blueprint, __name__, path to our static folder and templates folder
all_notes_blueprint = Blueprint("all_notes_blueprint", __name__, static_folder="static", template_folder="templates")


@all_notes_blueprint.route("/")
def default():
    all_notes = wild_plants_collection.find({ "thumb" : { "$ne": "" } })    #for note in all_notes:
    #    if not hasattr(note, 'thumb'):
    #        note["thumb"] = "placeholder.jpg"
    #    print(note)
    return render_template("allnotes.html", all_notes=all_notes)