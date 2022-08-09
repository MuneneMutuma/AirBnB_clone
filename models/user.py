#!/usr/bin/env python3
"""Module for User Model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for User Model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
