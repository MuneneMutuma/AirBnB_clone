#!/usr/bin/env python3
"""Module for Review Model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for Review model

    """
    def __init__(self, *args, **kwargs):
        """Constructor for Review Model

        """
        super().__init__(*args, **kwargs)
        if kwargs is None or len(kwargs) <= 0:
            self.place_id = ""
            self.user_id = ""
            self.text = ""
