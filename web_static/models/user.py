#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user in a lodging system.

    Attributes:
        __tablename__: Table name for users.
        email: User's email.
        password: User's password.
        first_name: User's first name.
        last_name: User's last name.
        places: Owned places.
        reviews: Written reviews.
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
