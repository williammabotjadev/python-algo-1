# Class inheritance

import math 

class Shape(Object):
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x 
        self.y = y 

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 

    