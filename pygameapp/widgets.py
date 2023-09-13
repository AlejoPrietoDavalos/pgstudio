""" Este módulo contiene la clase base para widgets. """
from __future__ import annotations
from abc import ABC, abstractmethod

import pygame as pg

class Widget(ABC):
    """ Clase abstracta para widgets."""

    @abstractmethod
    def is_mouse_up(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

class Widget:
    pass


# -----Revisar
class Block(pg.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pg.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pg.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
