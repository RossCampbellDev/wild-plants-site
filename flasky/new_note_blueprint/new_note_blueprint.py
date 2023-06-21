from flask import Blueprint, render_template, request
from flasky import wild_plants_collection
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
        "notes":request.form["notes-input-text"]
    }

    # create an object for the tags
    tag_array = []
    tags = request.form["tags-input-text"] or None
    if tags:
        for tag in tags.split(" "):
            tag_array.append(tag)

        new_note["tags"] = tag_array
        print(tag_array)
    else:
        new_note["tags"] = ""

    # TODO: avoid this sitaution
    photo = request.form["photo-input-text"]
    if photo != None:
        new_note["thumb"] = request.form["photo-input-text"]
    else:
        new_note["thumb"] = "placeholder.jpg"

    # add our new note to the collection
    new_id = wild_plants_collection.insert_one(new_note)

    return render_template("new_note/submitnewnote.html", new_note=new_note)

