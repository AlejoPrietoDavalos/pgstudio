from pygameapp.window import Window

import pygame as pg

from abc import ABC, abstractmethod

import attr
from attr.validators import instance_of

from typing import NewType
BBoxTuple = NewType("(x,y,w,h)", tuple[int,int,int,int])

@attr.s
class BBox:
    x: int = attr.ib(validator=instance_of(int))
    y: int = attr.ib(validator=instance_of(int))
    w: int = attr.ib(validator=instance_of(int))
    h: int = attr.ib(validator=instance_of(int))

    @property
    def bbox(self) -> BBoxTuple:     # TODO: Tipar.
        return (self.x, self.y, self.w, self.h)


class Drawable(Window, ABC):
    """ Todo objeto que pueda ser pintado en una `Scene`."""
    @abstractmethod
    def draw(self) -> None:
        """ Especifica la forma en que se usa `self.win` para dibujar."""
        ...


@attr.s
class BoxDrawable(BBox, Drawable):
    color_fill: tuple[int, int, int] = attr.ib(validator=instance_of(tuple))    # FIXME: Chequear 3 ints.

    def draw(self) -> None:
        pg.draw.rect(self.win, self.color_fill, self.bbox)

