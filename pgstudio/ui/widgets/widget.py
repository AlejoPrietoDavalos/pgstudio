""" Este módulo contiene la clase base para widgets. """
from __future__ import annotations
__all__ = ["Widget"]

from pgstudio.ui.abc.base import VisualElem

from abc import ABC, abstractmethod




class Widget(VisualElem, ABC):
    """ Clase abstracta para widgets."""
    @abstractmethod
    def draw(self) -> None: ...
    @abstractmethod
    def update(self) -> None: ...







































# -----Revisar
#import pygame as pg
#class Block(pg.sprite.Sprite):
#
#    # Constructor. Pass in the color of the block,
#    # and its x and y position
#    def __init__(self, color, width, height):
#       # Call the parent class (Sprite) constructor
#       pg.sprite.Sprite.__init__(self)
#
#       # Create an image of the block, and fill it with a color.
#       # This could also be an image loaded from the disk.
#       self.image = pg.Surface([width, height])
#       self.image.fill(color)
#
#       # Fetch the rectangle object that has the dimensions of the image
#       # Update the position of this object by setting the values of rect.x and rect.y
#       self.rect = self.image.get_rect()