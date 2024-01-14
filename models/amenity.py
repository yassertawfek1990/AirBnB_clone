#!/usr/bin/python3
"""Defines theAmenitclass."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent anamenity.

    Attributes:
        name (str): Thenameoftheamenity.
    """

    name = ""
