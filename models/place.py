#!/usr/bin/env python3
"""Module for Place Model
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Model class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitue = 0.0
    longitude = 0.0
    amenities_ids = list()
