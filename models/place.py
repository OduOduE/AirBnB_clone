#!/usr/bin/python3
""" Module for the Place model """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implements the Place model:

    Args:
        city_id (str): ID of the city
        user_id (str): ID of the user
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms of the place
        number_bathrooms (int): number of bathrooms of the place
        max_guest (int): maximum number of guests of the place
        price_by_night (int): Night price of the place
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (list): List of amenity ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
