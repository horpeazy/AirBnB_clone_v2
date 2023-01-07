#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models import FileStorage


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    # relationships
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", back_populates="place",
                            cascade="save-update, merge, delete")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
        cities = relationship("City", back_populates="places")
    else:
        @property
        def reviews(self):
            """ getter method for cities """
            reviews = []
            models = FileStorage.all()
            for obj in models.values():
                if type(obj["__class__"]) == Review and obj.place_id == self.id:
                    reviews.append(obj)
            return reviews

        @property
        def amenities(self):
            """ getter for amenities """
            amenities = []
            models = FileStorage.all(Amenity)
            for obj in models.values():
                if obj.id in self.amenity_ids:
                    amenities.append(obj)

            return amenities

        @amenities.setter
        def amenities(self, cls=None):
            """ setter method for amenities """
            if type(cls) == Amenity and cls.id not in self.amenity_ids:
                self.amenity_ids.append(cls.id)


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", ForeignKey("places.id"), primary_key=True, nullable=False),
    Column("amenity_id", ForeignKey("amenities.id"), primary_key=True, nullable=False)
)