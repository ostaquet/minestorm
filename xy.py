import math


class XY:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __copy__(self):
        new_obj = XY(self.x, self.y)
        return new_obj

    def distance(self, other: 'XY') -> float:
        distance: float = math.sqrt(
            (float(self.x - other.x) ** 2.0) +
            (float(self.y - other.y) ** 2.0)
        )
        return distance
