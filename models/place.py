#!/usr/bin/python3
"""Defines the Place class."""

import models
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Represents a lodging place in a database.

    Attributes:
        __tablename__: Table name for places.
        city_id: City ID.
        user_id: Owner's ID.
        name: Place name.
        description: Place description.
        number_rooms: Number of rooms.
        number_bathrooms: Number of bathrooms.
        max_guest: Max guests.
        price_by_night: Nightly price.
        latitude: Latitude.
        longitude: Longitude.
        reviews: Linked reviews.
        amenities: Available amenities.
        amenity_ids: Linked amenity IDs.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, overlaps="place_amenities")
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked reviews."""
            return [review for review in
                    list(models.storage.all(Review).values())
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Get/set linked amenities."""
            return [amenity for amenity in
                    list(models.storage.all(Amenity).values())
                    if amenity.id == self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
