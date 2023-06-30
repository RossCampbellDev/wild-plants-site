from flask import Blueprint, render_template, request
from flasky import logged_in
from flasky.note_model import Note
from werkzeug.utils import secure_filename
from flasky.photo_upload.photo_uploading import upload_thumbnail, upload_picture
import datetime

# name of the blueprint, __name__, path to our static folder and templates folder
new_note_blueprint = Blueprint("new_note_blueprint", __name__, static_folder="static", template_folder="templates")

photo_upload_dir = "../static/images/photos/"
thumb_upload_dir = "../static/images/thumbnails/"
photo_extensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@new_note_blueprint.route("/")
@logged_in
def default():
    datenow = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template("new_note/newnote.html", datenow=datenow)    # TODO: why do i need to specify new_note/ here but in all_notes_blueprint it uses relative path?


@new_note_blueprint.route("/submit-new", methods=['POST'])
@logged_in
def new_note():
    data = request.form

    title = data.get("title-input-text")
    date = data.get("date-input-text")
    location = data.get("location-input-text")
    notes = data.get("notes-input-text")
    tags = [t.lstrip() for t in data.get("tags-input-text").split(" ")]

    # TODO: get the user id properly for new notes
    user_id = "649994eed5f207baa6eecfb2"

    new_note = Note(
        title=title, notes=notes, location=location, tags=tags, date=date, picture="", thumb="", user_id=user_id
    )
    new_id = str(new_note.save())

    # handling the image upload
    picture="placeholder.jpg"
    picture_file = request.files["picture-input-file"]
    if picture_file.filename != '':
        new_note.picture = upload_picture(picture_file, new_id)
        if new_note.picture != False:
            new_note.thumb = upload_thumbnail(picture_file, new_id)
        else:
            print("error uploading picture") #TODO: error handling -> delete the document we just added

    new_note.debug()
    new_note.update()

    return render_template("new_note/submitnewnote.html", new_note=new_note)

