from flask import Blueprint, render_template, request, session
from flasky.note_model import Note
from flasky.photo_upload.photo_uploading import upload_thumbnail, upload_picture
from flasky import logged_in


all_notes_blueprint = Blueprint("all_notes_blueprint", __name__, static_folder="static", template_folder="templates")


@all_notes_blueprint.route("/")
@logged_in
def default(search_results=None):
    if not search_results:
        all_notes = Note.get_by_user_id(session["user_id"])
    else:
        all_notes = search_results
    return render_template("allnotes.html", all_notes=all_notes, username=session["username"])


@all_notes_blueprint.route("/editnote", methods=["GET", "POST"])
@logged_in
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
@logged_in
def update_note():
    data = request.form
    _id = data.get("id-input-text")
    title = data.get("title-input-text")
    date = data.get("date-input-text")
    location = data.get("location-input-text")
    notes = data.get("notes-input-text")
    tags = [t.lstrip() for t in data.get("tags-input-text").split(" ")]

    update_note = Note.get_by_id(_id)
    print(update_note)

    # handling the image upload
    picture = update_note["picture"]
    thumb = update_note["thumb"] or "placeholder.jpg"
    picture_file = request.files["picture-input-file"]

    if picture_file.filename != '' and picture_file.filename != update_note["picture"]:
        picture = upload_picture(picture_file, _id)
        if picture != False:
            thumb = upload_thumbnail(picture_file, _id)
        else:
            print("error uploading picture") #TODO: error handling

    # back to creating the note document for mongodb
    update_note = Note(
        user_id=session["user_id"],
        title=title,
        notes=notes,
        location=location,
        tags=tags,
        date=date,
        picture=picture,thumb=thumb
    )
    
    update_note._id = _id
    update_note.update()
    return default()


@all_notes_blueprint.route("/deletenote", methods=["POST"])
@logged_in
def delete_note():
    data = request.form
    id = data.get("id-input-text")
    delete_note = Note.get_instance(Note.get_by_id(id))
    if delete_note:
        delete_note.delete()
    return default()


@all_notes_blueprint.route("/searchnotes", methods=["POST"])
@logged_in
def search_notes():
    data = request.form
    tags = data.get('tag-input-text').split(' ')
    if tags[0]:
        tags = ["#" + tag if "#" not in tag else tag for tag in tags]
    else:
        tags = []
    location = data.get('location-input-text')
    search_date = data.get('date-input-text')

    search_results = Note.get_search_results(tags, location, search_date, session["user_id"])

    return render_template("allnotes.html", 
                           all_notes=search_results, 
                           username=session["username"], 
                           tags=' '.join(tags),
                           location=location,
                           search_date=search_date)
