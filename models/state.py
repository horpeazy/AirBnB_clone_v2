#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="save-update, merge, delete")

    @property
    def cities(self):
        from models import storage
        """ getter method for cities """
        cities = []
        models = storage.all()
        for obj in models.values():
            if type(obj) == City and obj.state_id == self.id:
                cities.append(obj)
        return cities
