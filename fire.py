import math

import pygame.draw
from pygame import Surface

from color_palette import ColorPalette
from xy import XY
from item import Item


class Fire(Item):

    def __init__(self, window: Surface, position: tuple[float, float], angle: float, max_distance: float = 200,
                 speed: float = 15):
        super().__init__(window, XY(position[0], position[1]))

        self._origin: XY = self._position.__copy__()
        self._angle: float = angle

        self._max_distance: float = max_distance

        self._velocity: XY = XY(-round(math.sin(math.radians(self._angle)), 2) * speed,
                                -round(math.cos(math.radians(self._angle)), 2) * speed)

    def draw(self):
        surface: Surface = Surface((3, 3))

        pygame.draw.circle(surface, ColorPalette.fire, (1, 1), 2)

        self._position.x = self._position.x + self._velocity.x
        self._position.y = self._position.y + self._velocity.y

        self._window.blit(surface, (self._position.x, self._position.y))

    def is_exist(self):
        if not super().is_exist():
            return False

        if self._position.distance(self._origin) > self._max_distance:
            return False

        return True
