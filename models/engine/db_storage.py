#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import text
from models.base_model import Base
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


HBNB_MYSQL_USER = os.environ.get("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = os.environ.get("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = os.environ.get("HBNB_MYSQL_HOST")
HBNB_MYSQL_DB = os.environ.get("HBNB_MYSQL_DB")
HBNB_ENV = os.environ.get("HBNB_ENV")


class DBStorage:
    """ This class manages storage of hbnb models in the database """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """ initialize the database """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB
        ), pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of models currently in storage """
        classes = {"User": User, "State": State, "City": City, 
                        "Amenity": Amenity, "Place": Place , "Review": Review
        }
        if not cls:
            dictionary = {}
            for obj_name, obj in classes.items():
                objs = self.__session.query(obj.__table__).all()
                for item in objs:
                    key = obj_name  + "." + item.id           
                    dictionary.update({key: item})
        else:
            dictionary = {}
            cls = classes[cls]
            objs = self.__session.query(cls.__table__).all()
            for item in objs:
                    key = obj + "." + item.id
                    dictionary.update({key: item})

        return dictionary

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the storage dictionary """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create tables and sessions """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit =False)()
