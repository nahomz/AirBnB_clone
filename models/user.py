#!/user/usr/python3
"""module for User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """instantiation of user"""
        super().__init__(*args, **kwargs)
