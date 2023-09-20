from __future__ import annotations

from pygameapp.window import Window

import pygame as pg

from abc import ABC, abstractmethod

import attr
from attr.validators import instance_of

from typing import NewType
BBoxList = NewType("[x,y,w,h]", list[int,int,int,int])


class BBox(ABC):
    def __init__(self, bbox: BBoxList):
        assert isinstance(bbox, list) and len(bbox)==4 \
            and all(isinstance(c, int) for c in bbox)
        self.bbox = bbox
    
    @property
    def x(self) -> int: return self.bbox[0]
    @property
    def y(self) -> int: return self.bbox[1]
    @property
    def w(self) -> int: return self.bbox[2]
    @property
    def h(self) -> int: return self.bbox[3]



class Drawable(Window, ABC):
    """ Todo objeto que pueda ser pintado en una `Scene`."""
    @abstractmethod
    def draw(self) -> None:
        """ Especifica la forma en que se usa `self.win` para dibujar."""
        ...


class BoxDrawable(BBox, Drawable):
    # FIXME: Chequear 3 ints.
    def __init__(self, bbox: BBoxList, color_fill: tuple[int, int, int]):
        super().__init__(bbox)
        self.color_fill = color_fill
    
    def draw(self) -> None:
        pg.draw.rect(self.win, self.color_fill, self.bbox)
    
    def move(self, bbox_delta: BBoxList) -> None:
        self.bbox = [c+c_delta for c, c_delta in zip(self.bbox, bbox_delta)]
        