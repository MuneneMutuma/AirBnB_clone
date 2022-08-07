#!/usr/bin/env python3
"""Module for State Model
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Model class
    """
    def __init__(self, *args, **kwargs):
        """Constructor for State Model

        Attr:
            *args (list):       list of ordered arguments
            **kwargs (dict):    map for key-worded arguments
        """
        super().__init__(*args, **kwargs)
        if kwargs is None or len(kwargs) <= 0:
            self.name = ""
