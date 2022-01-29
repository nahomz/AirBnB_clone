#!/usr/bin/python3
"""module for State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes class State"""
        super().__init__(*args, **kwargs)
