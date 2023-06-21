import datetime
from pymongo import MongoClient
from pymongo.errors import PyMongoError

import os
from dotenv import load_dotenv
load_dotenv()
MONGO_CONN_STRING = os.environ.get('MONGO_CONN_STRING')

client = MongoClient(MONGO_CONN_STRING)
db = client["wild-plants"]
wild_plants_collection = db["wild-plants-collection"]

class Note:
    def __init__(self, title, notes, location, tags, date=datetime.datetime.now().strftime("%Y-%m-%d"), picture="placeholder.jpg"):
        self.title = title
        self.date = date
        self.notes = notes
        self.location = location
        self.tags = tags
        self.picture = picture
        self.thumb = picture    # TODO: sort this

    def debug(self):
        for attr, value in vars(self).items():
            print(f"{attr}: {value}")

    def save(self):
        note_data = {
            'title': self.title,
            'date': self.date,
            'notes': self.notes,
            'location': self.location,
            'tags': self.tags,
            'picture': self.picture,
            'thumb': self.picture   # TODO: auto save and resize image, then get thumb fname
        }
        try:
            self._id = wild_plants_collection.insert_one(note_data).inserted_id
        except PyMongoError as e:
            print(f'ERROR DURING INSERT: {str(e)}')

        return self._id

    @staticmethod
    def get_all():
        return list(wild_plants_collection.find())

    @staticmethod
    def get_by_title(title):
        return wild_plants_collection.find_one({'title': title})

    @staticmethod
    def get_by_tags(tags):
        return wild_plants_collection.find({'tags': { '$in': tags}})

    @staticmethod
    def get_by_date(date):
        return wild_plants_collection.find({'date': { '$gte': date }})

    def update(self):
        note_data = {
            'title': self.title,
            'date': self.date,
            'notes': self.notes,
            'location': self.location,
            'tags': self.tags,
            'picture': self.picture,
            'thumb': self.picture   # TODO: sort
        }
        return wild_plants_collection.update_one({'_id': self._id}, {'$set': note_data})

    def delete(self):
        return wild_plants_collection.delete_one({'_id': self._id})
