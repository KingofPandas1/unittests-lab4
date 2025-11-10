
import math


import math

def area(r):
    if r < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * r * r

def perimeter(r):
    if r < 0:
        raise ValueError("radius must be non-negative")
    return 2 * math.pi * r