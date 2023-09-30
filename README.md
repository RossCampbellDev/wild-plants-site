# tasks
## mongodb
✅ conn string -> env vars 

✅ flask app connect to db 

✅ read notes into python 

✅ model/view stuff!? [mongo alternative] 

⭕ input validation/sanitisation

✅ user model

## review all
✅ read from json array 

✅ display in nice grid 

✅ get thumb image to show 

✅ fix grid so it's more evenly distributed 

✅ the note body text is no longer hidden?

### view note overlay
✅ click on an existing note and see the full description and details?

## new note
✅ date picker 

✅ form submit 

✅ save array from tags 

✅ save to mongodb 

✅ photo upload 

✅ create thumbnail image with square ratio

    ✅ doesn't seem to always crop - because of size perhaps?

✔ error handling for picture file uploads

✅ better handle 'success' eg nicer transition after new note created

⭕ make it PRETTIER - convert to slideshow?

## edit note
✅ change any field value 

✅ delete 

⭕ confirmation for deletion

✅ remove image when deleting or changing! (notemodel)

⭕ remove attached image?

✅ see existing image on this screen


## user system
✅ user login

✅ user session - change in __init__.py decorator function

✅ create user (hash password)

✅ check for logged in, display "log in" or "sign up" or go straight to new note

✅ retrieve user notes

✅ redirect to login on all other screens, if nobody is logged in (custom decorator)

⭕ session time out

✅ log out button


## search system
✅ tags

✅ search by location??

✅ filter(s) on review all screen

⭕ ordering results on review all

## CI/CD
```
sudo docker create volume mongo-plants-volume

sudo docker run -d -p27017:27017 \
--name=mongo-plants \
-e MONGO_INITDB_ROOT_USERNAME=root \
-e MONGO_INITDB_ROOT_PASSWORD=<PASS> \
-e MONGO_INITDB_DATABASE=wild-plants \
--restart always \
-v mongo-plants-volume:/data/db \
mongo:latest
```

to access the shell while running and set up user permissions:
'''
sudo docker exec -it mongo-plants mongosh
db.auth("root")
use wild-plants
db.createUser({user:"radaghast", pwd:<PASS>, roles: [{ role:"readWrite", db:"wild-plants"}]})
```

## connectivity - app server to db server
running mongodb container with persistent storage - IP on this host is 172.17.0.2:27017
the app container is running on 172.17.0.3 and they communicate between each other
in future will need to do port forwarding on NAT when they are running on separate machines

⭕ but in app i am using the global root credentials to get permission on mongo in general.  not using radaghast at present