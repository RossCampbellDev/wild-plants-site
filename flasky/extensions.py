from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_CONN_STRING = os.environ.get('MONGO_CONN_STRING')

client = MongoClient(MONGO_CONN_STRING)
db = client["wild-plants"]