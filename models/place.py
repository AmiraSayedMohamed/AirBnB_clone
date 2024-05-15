#!/user/bin/python3

""" This is a module creates a Place Class
A subclass of BaseModel class
"""

class place(BaseModel):
    """
    A class for managing place objects, subclass of BaseModel
    Public class attributes:
    city_id: (str)
    name: (str)
    user_id: (str)
    description: (str)
    number_rooms: (int)
    max_guest: (int)
    number_bathrooms: (int)
    price_by_night: (int)
    latitude: (float)
    longitude: (float)
    amenity_ids: (list)
    """
    amenity_ids = []
    longitude = 0.0
    latitude = 0.0
    price_by_night = 0
    max_guest = 0
    number_bathrooms = 0
    number_rooms = 0
    description = ""
    name = ""
    user_id = ""
    city_id = ""
