#!/usr/bin/env python3
"""Module for User Model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for User Model
    """
    def __init__(self, *args, **kwargs):
        """Constructor for User Model
        """
        super().__init__(*args, **kwargs)
        if kwargs is None or len(kwargs) <= 0:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
