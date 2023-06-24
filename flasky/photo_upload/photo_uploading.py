from werkzeug.utils import secure_filename
from PIL import Image
import os

# PHOTO UPLOAD UTILS
photo_upload_dir = "flasky/static/images/photos/"
thumb_upload_dir = "flasky/static/images/thumbnails/"
photo_extensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def check_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in photo_extensions

def upload_picture(picture_file, _id):
    if picture_file and check_extension(picture_file.filename):     # make sure valid file type
        picture = _id+'_'+secure_filename(picture_file.filename)    # security check
        picture_file.save(os.path.join(photo_upload_dir, picture))  # physically save the file
        return True
    return False

def generate_thumbnail(picture_file):
    print("1")