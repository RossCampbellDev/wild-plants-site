from flask import Blueprint, render_template, request

# name of the blueprint, __name__, path to our static folder and templates folder
all_notes_blueprint = Blueprint("all_notes_blueprint", __name__, static_folder="static", template_folder="templates")


@all_notes_blueprint.route("/")
def default():
    all_notes = [
        {"title": "Look at this bridge", "date": "2023-05-23", "thumb": "thumb_01.jpg" , "description": "this is over in New Mills :D"},
        {"title": "Some pink thing",    "date": "2023-09-10", "thumb": "thumb_02.jpg", "description": "WOWEEEE a pink thing!"},
        {"title": "FIRE PETALS",        "date": "2023-04-16", "thumb": "thumb_03.jpg", "description": "THIS PLANT LOOKS LIKE FIRE.  notes notes notes lots of fake notes to take up some spaaaace"},
        {"title": "Pirckly Thistle",    "date": "2023-03-29", "thumb": "thumb_04.jpg", "description": "this is a cool image of some stuuuuuuuuuuuuuuuff!"},
        {"title": "note title 05",      "date": "2023-07-08", "thumb": "thumb_05.jpg", "description": "this is a cool image of some stuuuuuuuuuuuuuuuff!"},
        {"title": "note title 06",      "date": "2023-02-02", "thumb": "thumb_06.jpg", "description": "this is a cool image of some stuuuuuuuuuuuuuuuff!"},
        {"title": "note title 07",      "date": "2023-10-14", "thumb": "thumb_07.jpg", "description": "this is a cool image of some stuuuuuuuuuuuuuuuff!"},
        {"title": "note title 08",      "date": "2023-06-05", "thumb": "thumb_08.jpg", "description": "this is a cool image of some stuuuuuuuuuuuuuuuff!"},
        {"title": "note title 09",      "date": "2023-08-19", "thumb": "thumb_09.jpg", "description": "this is a cool image of some stuuuuuuuuuuuuuuuff!"},
        {"title": "note title 10",      "date": "2023-01-11", "thumb": "thumb_10.jpg", "description": "this is a cool image of some stuuuuuuuuuuuuuuuff!"}
    ]


    # get all the notes data and pass through
    return render_template("allnotes.html", all_notes=all_notes)