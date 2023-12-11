"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User for the HBnB project."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

