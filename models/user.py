#!/usr/bin/python3
""" Implements the user's model """
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from the BaseModel class and adds user functionalities:

    Args:
        email (str): the user's email
        password (str): user's password
        first_name (str): user's first name
        last_name (str): user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
