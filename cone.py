# Programmer: 
# Description: 

from math import pi
from math import hypot

def get_volume (radius,height):
    volume = (pi * radius ** 2 * height) / 3
    return volume

def get_surface_area (radius, height):
    slant_height = hypot(radius,height)
    area = pi * radius ** 2 + pi * radius * slant_height
    return area

