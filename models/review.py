#!/usr/bin/env python3
"""Module for Review Model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for Review model

    """
    place_id = ""
    user_id = ""
    text = ""
