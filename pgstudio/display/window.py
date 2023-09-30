from __future__ import annotations
__all__ = ["Window"]

import pygame as pg
from pygame.surface import Surface

from abc import ABC, abstractmethod

from typing import NewType
WinRes = NewType("win_resolution", tuple[int, int])

class Window(ABC):
    win: Surface
    resolution: WinRes
    
    @classmethod
    def set_win(cls, resolution: WinRes) -> None:
        Window.win = pg.display.set_mode(resolution)
        Window.resolution = resolution

    # @classmethod
    # def pix2prop(cls, pix: int) -> float: return cls.resolution
    # @classmethod
    # def prop2pix(): pass



