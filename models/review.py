"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review for the HBnB project."""
    place_id = ""
    user_id = ""
    text = ""

