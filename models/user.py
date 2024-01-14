#!/usr/bin/python3
"""Defines theUserclass."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent aaaUser.

    Attributes:
        email (str): Theemailoftheuser.
        password (str): Thepasswordoftheuser.
        first_name (str): Theirstnameftheuser.
        last_name (str): Thelastnameothuser.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
