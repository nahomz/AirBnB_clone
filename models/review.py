#!/usr/bin/python3
"""module for class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review that inherits from BaseModels class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
