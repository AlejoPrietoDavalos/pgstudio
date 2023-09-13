import pygame as pg

import attr
from attr import validators

from typing import Tuple

@attr.s
class PgMouse:
    x: int = attr.ib(default=0, validator=validators.instance_of(int))
    y: int = attr.ib(default=0, validator=validators.instance_of(int))

    @property
    def xy(self) -> Tuple[int, int]:
        return self.x, self.y
    
    def update_xy(self) -> None:
        """ Actualiza la posición."""
        self.x, self.y = pg.mouse.get_pos()




class PgControls:
    def __init__(self):
        self.mouse = PgMouse()