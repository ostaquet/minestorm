import random

import pygame.draw
from pygame import Surface

from color_palette import ColorPalette
from item import Item
from xy import XY


class Enemy(Item):
    def __init__(self, window: Surface):
        super().__init__(window,
                         XY(random.randint(0, self._window.get_width()),
                            random.randint(0, self._window.get_height())))

        self._velocity: XY = XY(random.randint(-5, 5), random.randint(-5, 5))

    def draw(self):
        surface: Surface = Surface((50, 50))
        pygame.draw.circle(surface, ColorPalette.enemy, (25, 25), 25)

        self._position.x = self._position.x + self._velocity.x
        self._position.y = self._position.y + self._velocity.y

        self._window.blit(surface, (self._position.x, self._position.y))
