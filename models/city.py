#!/usr/bin/python3
""" module for City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from class BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
