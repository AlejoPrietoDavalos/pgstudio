import pygame as pg

import attr

@attr.s
class PgMouse:
    x: int = attr.ib(default=pg.mouse.get_cursor) # TODO: Algo así.
    y: int = attr.ib(default=pg.mouse.get_cursor) # TODO: Algo así.

    def recalcular(self):
        return #pg.




