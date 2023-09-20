import pygame as pg
from pygame.surface import Surface

from abc import ABC, abstractmethod

class Window(ABC):
    win: Surface
    resolution: tuple[int, int]
    
    @classmethod
    def set_win(cls, resolution: tuple[int, int]) -> None:
        Window.win = pg.display.set_mode(resolution)
        Window.resolution = resolution

    @classmethod
    def pix2prop(cls, pix: int, pix_is_x) -> float:
        return cls.resolution
    
    @classmethod
    def prop2pix():
        pass

class Drawable(Window, ABC):
    """ Todo objeto que pueda ser pintado en una `Scene`."""
    pass

