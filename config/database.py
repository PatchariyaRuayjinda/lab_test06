from pymongo import MongoClient
import ssl
from core import config

ssl._create_default_https_context = ssl._create_unverified_context

client = MongoClient("mongodb+srv://"+config.settings.user_name+":"+config.settings.pass_word+"@"+config.settings.host+"/myFirstDatabase?retryWrites=true&w=majority")


db = client.todo_app

collection_name = db["todos_app"]
courses_collection = db["courses"]
