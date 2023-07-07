from werkzeug.utils import secure_filename
from PIL import Image
import os

# PHOTO UPLOAD UTILS
photo_upload_dir = "flasky/static/images/photos/"
thumb_upload_dir = "flasky/static/images/thumbnails/"
photo_extensions = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])

def check_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in photo_extensions

def upload_picture(picture_file, _id):
    if picture_file and check_extension(picture_file.filename):
        fname = _id+'_'+secure_filename(picture_file.filename)    # security check
        picture_file.save(os.path.join(photo_upload_dir, fname))
        return fname
    return False

def upload_thumbnail(picture_file, _id):
    with Image.open(picture_file) as picture:
        thumbnail = picture

        size = min(thumbnail.size)
        left = (thumbnail.width - size) // 2
        top = (thumbnail.height - size) // 2
        right = left + size
        bottom = top + size
        
        cropped = thumbnail.crop((left, top, right, bottom))
        resized = cropped.resize((200, 200))

        fname = _id+'_thumb_'+secure_filename(picture_file.filename)
        resized.save(os.path.join(thumb_upload_dir, fname))
        return fname