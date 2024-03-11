import math

import pygame.draw
from pygame import Surface, Rect

from color_palette import ColorPalette
from xy import XY


class Starship:

    def __init__(self, window: Surface,
                 max_speed: float = 10, boost_speed: float = 0.5, angle_speed: float = 5, brake_speed: float = 1):

        self._window: Surface = window
        self._position: XY = XY(window.get_rect().width / 2, window.get_rect().height / 2)
        self._size: int = 31

        self._max_speed: float = max_speed
        self._boost_speed: float = boost_speed
        self._angle_speed: float = angle_speed
        self._brake_speed: float = brake_speed

        self._speed: XY = XY(0, 0)
        self._angle: int = 0

    def boost(self):
        # Based on trigonometric circle
        motion: XY = XY(-round(math.sin(math.radians(self._angle)), 2) * self._boost_speed,
                        -round(math.cos(math.radians(self._angle)), 2) * self._boost_speed)

        if abs(self._speed.x + motion.x) > self._max_speed or abs(self._speed.y + motion.y) > self._max_speed:
            return

        self._speed.x = self._speed.x + motion.x
        self._speed.y = self._speed.y + motion.y

    def brake(self):
        if abs(self._speed.x) > self._brake_speed or abs(self._speed.y) > self._brake_speed:
            return

        self._speed.x = 0
        self._speed.y = 0

    def turn_left(self):
        self._angle = self._angle + self._angle_speed
        if self._angle >= 360:
            self._angle = self._angle - 360

    def turn_right(self):
        self._angle = self._angle - self._angle_speed
        if self._angle < 0:
            self._angle = 360 + self._angle

    def draw(self):
        surface: Surface = Surface((self._size, self._size))

        # Draw the starship
        points: list[tuple[float, float]] = [
            (self._size/2, 0),
            (0, self._size),
            (self._size/2, self._size * 0.8),
            (self._size, self._size)
        ]

        pygame.draw.lines(surface, ColorPalette.starship, True, points)

        # Compute the position
        self._position.x = self._position.x + self._speed.x
        self._position.y = self._position.y + self._speed.y

        if self._position.x < 0:
            self._position.x = self._window.get_width() + self._position.x
        if self._position.x > self._window.get_width():
            self._position.x = self._position.x - self._window.get_width()
        if self._position.y < 0:
            self._position.y = self._window.get_height() + self._position.y
        if self._position.y > self._window.get_height():
            self._position.y = self._position.y - self._window.get_height()

        surface = pygame.transform.rotate(surface, self._angle)

        surface_rect: Rect = surface.get_rect()
        surface_rect.centerx = self._position.x
        surface_rect.centery = self._position.y

        self._window.blit(surface, surface_rect)

    def debug(self) -> str:
        debug_msg: str = (f"Starship: pos({self._position.x},{self._position.y}) "
                          f"angle({self._angle}°) speed({self._speed.x},{self._speed.y})")
        return debug_msg

    def get_pos(self) -> tuple[float, float]:
        return self._position.x, self._position.y

    def get_angle(self) -> float:
        return self._angle
