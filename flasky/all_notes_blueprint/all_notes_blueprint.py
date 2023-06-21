from flask import Blueprint, render_template, request
from flasky.note_model import Note


# name of the blueprint, __name__, path to our static folder and templates folder
all_notes_blueprint = Blueprint("all_notes_blueprint", __name__, static_folder="static", template_folder="templates")


@all_notes_blueprint.route("/")
def default():
    all_notes = Note.get_all()
    return render_template("allnotes.html", all_notes=all_notes)


@all_notes_blueprint.route("/editnote", methods=["GET", "POST"])
def edit_note():
    if request.method == "GET":
        return default() # shouldn't be here naughty!    
    data = request.form
    edit_note = Note.get_by_id(data.get("note-to-edit"))
    
    if edit_note["tags"]:
        if len(edit_note["tags"]) > 1:
            edit_note["tags"] = ' '.join(edit_note["tags"])
        else:
            edit_note["tags"] = edit_note["tags"][0]
    else:
        edit_note["tags"] = ""
    return render_template("editnote.html", edit_note=edit_note)


@all_notes_blueprint.route("/updatenote", methods=["POST"])
def update_note():
    data = request.form
    title = data.get("title-input-text")
    date = data.get("date-input-text")
    location = data.get("location-input-text")
    notes = data.get("notes-input-text")
    picture = data.get("picture-input-text") or "placeholder.jpg"
    # TODO: thumb
    tags = [t.lstrip() for t in data.get("tags-input-text").split(" ")]

    update_note = Note(
        title=title, notes=notes, location=location, tags=tags, date=date, picture=picture
    )
    
    update_note._id = data.get("id-input-text")
    update_note.update()
    return default()