#!/usr/bin/python3
"""Defines the City class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a city in a database.

    Attributes:
        __tablename__: Table name for cities.
        name: City name.
        state_id: State ID.
        places: Relationship with Place class.
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship(
        "Place",
        backref="city",
        cascade="delete",
        passive_deletes=True
    )
