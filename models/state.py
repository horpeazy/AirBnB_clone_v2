#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="save-update, merge, delete")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @property
    def cities(self):
        """ getter method for cities """
        cities = []
        models = FileStorage.all()
        for obj in models.values():
            if type(obj["__class__"]) == City and obj.state_id == self.id:
                cities.append(obj)
        return cities
