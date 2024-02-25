import math

import pygame.draw
from pygame import Surface, Rect

from color_palette import ColorPalette


class Fire:

    def __init__(self, window: Surface,
                 position: tuple[float, float], angle: float,
                 max_distance: float = 200, speed: float = 15):

        self._window = window

        self._origin: Rect = Rect(position[0], position[1], 1, 1)
        self._position: Rect = Rect(self._origin)
        self._angle: float = angle

        self._max_distance: float = max_distance

        self._velocity_x: float = -round(math.sin(math.radians(self._angle)), 2) * speed
        self._velocity_y: float = -round(math.cos(math.radians(self._angle)), 2) * speed

    def draw(self):
        surface: Surface = Surface((3, 3))

        pygame.draw.circle(surface, ColorPalette.fire, (1, 1), 2)

        self._position.x = self._position.x + self._velocity_x
        self._position.y = self._position.y + self._velocity_y

        self._window.blit(surface, (self._position.x, self._position.y))

    def is_exist(self):
        if self._position.x < 0:
            return False
        if self._position.x > self._window.get_width():
            return False
        if self._position.y < 0:
            return False
        if self._position.y > self._window.get_height():
            return False

        distance: float = math.sqrt(
            (float(self._position.x - self._origin.x) ** 2.0) +
            (float(self._position.y - self._origin.y) ** 2.0)
        )

        if distance > self._max_distance:
            return False

        return True
