from abc import abstractmethod

from pygame import Surface

from xy import XY


class Item:
    def __init__(self, window: Surface, position: XY):
        self._window = window
        self._position: XY = position

    @abstractmethod
    def draw(self):
        pass

    def is_exist(self):
        if self._position.x < 0:
            return False
        if self._position.x > self._window.get_width():
            return False
        if self._position.y < 0:
            return False
        if self._position.y > self._window.get_height():
            return False

        return True
