#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


HBNB_TYPE_STORAGE = os.environ.get("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
