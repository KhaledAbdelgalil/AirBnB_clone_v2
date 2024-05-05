#!/usr/bin/python3
"""Defines the State class."""

import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a state and its cities.

    Attributes:
        __tablename__: Table name for states.
        name: State name.
        cities: Relationship with City class.
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            return [city for city in list(models.storage.all(City).values())
                    if city.state_id == self.id]
