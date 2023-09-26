""" Geometrías para almacenar datos geométricos.
- TODO: Pasar todo a numpy, y ver si funciona en pygame.
"""
from __future__ import annotations
from pgstudio.geometry.abc import GeomBase, Vector

from pydantic import BaseModel, NonNegativeInt, validator, Field
from multipledispatch import dispatch

from collections.abc import Iterator, MutableSequence, Iterable
from abc import ABC, abstractmethod

from typing import (
    NewType, Tuple, List, SupportsIndex,
    NamedTuple, ClassVar, Union)

from pgstudio.geometry.typings import (
    XY_Tuple, XY_List, BoxList,
    CoordX, CoordY, Width, Height)



def is_xy(xy: XY_Tuple) -> bool:
    return isinstance(xy, tuple) and len(xy)==2 and \
       all(isinstance(c, int) for c in xy)

def is_point(point: Point) -> bool:
    return isinstance(point, Point)

def assert_xy(xy: XY_Tuple) -> None:
    assert is_xy(xy)

def assert_xy_list(xy_list: XY_List) -> None:
    assert isinstance(xy_list, list)
    assert all(is_xy(xy) for xy in xy_list)


#class Area(PointList):     # El último conecta con el primero. También hay que ver como chequear si las lineas se cortan.
#class Polygon(Area):
#class Vector(GeomBase):
#    pass

class Point(GeomBase):
    """
    - TODO: Ver si podría implementarse esto con numpy. Sería interesante.
    - FIXME: Ver como se puede encapsular el assert del xy.
    - FIXME: Ver como puedo hacer para que `xy` sea serializado y checkeado todo encapsulado.
    """
    xy: XY_Tuple
    def __init__(self, xy: XY_Tuple):
        super().__init__(xy=xy)

    @property
    def xy_ref(self) -> XY_Tuple: return self.x, self.y
    @property
    def x(self) -> CoordX: return self.xy[0]
    @property
    def y(self) -> CoordY: return self.xy[1]

    @staticmethod
    def serial(p: Point | XY_Tuple) -> Point:
        if is_point(p):
            return p
        elif is_xy(p):
            return Point(p)
        else:
            raise TypeError("Tipo incorrecto para `Point`.")
    
    def move(self, xy: XY_Tuple) -> None:
        """ FIXME"""
        assert_xy(xy)
        self.xy = xy
    
    def translation(self, v: Vector) -> None:
        """ FIXME"""
        self.xy = tuple([c + dc for (c, dc) in zip(self.xy, v)])
    
    def __eq__(self, other: Point) -> bool:
        return self.xy == other.xy
    #def __add__(self, other: Point) -> Point:
    #TODO: todas las operaciones


class Box(GeomBase):
    """
    - (x2, y2) = (x1+w, y1+h)
    - xy_tl=(x1,y1) +--------+ xy_tr=(x2,y1)
    - xy_bl=(x1,y2) +--------+ xy_br=(x2,y2)
    """
    box: BoxList = Field(frozen=True)
    def __init__(self, box: BoxList):
        super().__init__(box=box)
    
    #-----> `xy_ref` de referencia.
    @property
    def xy_ref(self) -> XY_Tuple: return self.xy_tl

    @property
    def x1(self) -> CoordX: return self.box[0]
    @property
    def y1(self) -> CoordY: return self.box[1]
    @property
    def w(self) -> Width: return self.box[2]
    @property
    def h(self) -> Height: return self.box[3]
    @property
    def x2(self) -> CoordX: return self.x1 + self.w
    @property
    def y2(self) -> CoordY: return self.y1 + self.h

    #-----> `XY_Tuple` de las 4 esquinas del rectángulo.
    @property
    def xy_tl(self) -> XY_Tuple: return self.x1, self.y1
    @property
    def xy_tr(self) -> XY_Tuple: return self.x2, self.y1
    @property
    def xy_br(self) -> XY_Tuple: return self.x2, self.y2
    @property
    def xy_bl(self) -> XY_Tuple: return self.x1, self.y2

    #-----> `Point` de las 4 esquinas del rectángulo.
    @property
    def p_tl(self) -> Point: return Point(xy=self.xy_tl)
    @property
    def p_tr(self) -> Point: return Point(xy=self.xy_tr)
    @property
    def p_br(self) -> Point: return Point(xy=self.xy_br)
    @property
    def p_bl(self) -> Point: return Point(xy=self.xy_bl)

    def intersects(self, point: XY_Tuple | Point) -> bool:
        """ True si el punto se encuentra dentro."""
        point = Point.serial(point)
        return (self.x1 <= point.x <= self.x2) and \
               (self.y1 <= point.y <= self.y2)

    def translation(self, v: Vector) -> None:
        # FIXME: POner un vector despues.
        dx, dy = v
        self.box[0] += dx
        self.box[1] += dy

    def move(self, xy: XY_Tuple) -> None:
        self.box[0], self.box[1] = xy












