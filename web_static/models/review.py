#!/usr/bin/python3
"""Defines the Review class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Represents a review for a lodging place.

    Attributes:
        __tablename__: Table name for reviews.
        text: Review content.
        place_id: ID of the reviewed place.
        user_id: ID of the reviewer.
    """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
