#!/usr/bin/env python3
"""Module for Place Model
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Model class
    """
    def __init__(self, *args, **kwargs):
        """Constructor for Place Model

        Attr:
            *args (list):       list of ordered arguments
            **kwargs (dict):    map for key-worded arguments
        """
        super().__init__(*args, **kwargs)
        if kwargs is None or len(kwargs) <= 0:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitue = 0.0
            self.longitude = 0.0
            self.amenities_ids = list()
