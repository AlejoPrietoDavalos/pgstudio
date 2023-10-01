from __future__ import annotations
__all__ = ["Window"]

import pygame as pg

from .typings import Win, WinRes


class Window:
    """ FIXME: Encapsular `win` y `resolution`."""
    _instance = None
    win: Win
    resolution: WinRes

    def __new__(cls, resolution: WinRes):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Window, cls).__new__(cls)
            cls.win = pg.display.set_mode(resolution)
            cls.resolution = resolution
        return cls._instance

    #def __init__(self)