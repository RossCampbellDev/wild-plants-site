from flask import Blueprint, render_template, request
from flasky.note_model import Note
from flasky.photo_upload.photo_uploading import generate_thumbnail, upload_picture
from werkzeug.utils import secure_filename
import datetime, os

# name of the blueprint, __name__, path to our static folder and templates folder
new_note_blueprint = Blueprint("new_note_blueprint", __name__, static_folder="static", template_folder="templates")

photo_upload_dir = "../static/images/photos/"
thumb_upload_dir = "../static/images/thumbnails/"
photo_extensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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

    picture = request.files["picture-input-file"]
    print(f'PICTURE: {picture}') #test
    # check photo file extension

    # TODO: thumb
    tags = [t.lstrip() for t in data.get("tags-input-text").split(" ")]

    new_note = Note(
        title=title, notes=notes, location=location, tags=tags, date=date, picture=picture
    )
    new_id = new_note.save()

    return render_template("new_note/submitnewnote.html", new_note=new_note)

