from flask import Blueprint, render_template, request
from flasky.note_model import Note
from flasky.photo_upload.photo_uploading import upload_thumbnail, upload_picture


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
    _id = data.get("id-input-text")
    title = data.get("title-input-text")
    date = data.get("date-input-text")
    location = data.get("location-input-text")
    notes = data.get("notes-input-text")
    tags = [t.lstrip() for t in data.get("tags-input-text").split(" ")]

    # handling the image upload
    picture="placeholder.jpg"
    picture_file = request.files["picture-input-file"]
    if picture_file.filename != '':
        picture = upload_picture(picture_file, _id)
        if picture != False:
            thumb = upload_thumbnail(picture_file, _id)
        else:
            print("error uploading picture") #TODO: error handling

    # back to creating the note document for mongodb
    update_note = Note(
        title=title, notes=notes, location=location, tags=tags, date=date, picture=picture, thumb=thumb
    )
    
    update_note._id = _id
    update_note.update()
    return default()


@all_notes_blueprint.route("/deletenote", methods=["POST"])
def delete_note():
    data = request.form
    id = data.get("id-input-text")
    delete_note = Note.get_instance(Note.get_by_id(id))
    if delete_note:
        delete_note.delete()
    return default()