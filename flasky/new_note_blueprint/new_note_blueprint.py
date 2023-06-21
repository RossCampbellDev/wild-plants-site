from flask import Blueprint, render_template, request
from flasky.note_model import Note
import datetime

# name of the blueprint, __name__, path to our static folder and templates folder
new_note_blueprint = Blueprint("new_note_blueprint", __name__, static_folder="static", template_folder="templates")


@new_note_blueprint.route("/")
def default():
    datenow = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template("new_note/newnote.html", datenow=datenow)


@new_note_blueprint.route("/submit-new", methods=['POST'])
def new_note():
    data = request.form
    title = data.get("title-input-text")
    date = data.get("date-input-text")
    location = data.get("location-input-text")
    notes = data.get("notes-input-text")
    picture = data.get("picture-input-text")
    tags = [t.lstrip() for t in data.get("tags-input-text").split(" ")]

    new_note = Note(
        title=title, notes=notes, location=location, tags=tags, date=date, picture=picture
    )
    new_id = new_note.save()
    new_note._id = new_id
    # add our new note to the collection
    #new_id = wild_plants_collection.insert_one(new_note)

    return render_template("new_note/submitnewnote.html", new_note=new_note)

