#!/usr/bin/python3
"""Defines theReviewclass."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): ThePlcid.
        user_id (str): TheUserid.
        text (str): Thetextofthereview.
    """

    place_id = ""
    user_id = ""
    text = ""
