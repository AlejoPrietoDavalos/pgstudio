""" Geometrías para almacenar datos geométricos."""
from __future__ import annotations

from pydantic import BaseModel, NonNegativeInt, validator, Field
from multipledispatch import dispatch

from collections.abc import Iterator, MutableSequence, Iterable
from abc import ABC, abstractmethod

from typing import (
    NewType, Tuple, List, SupportsIndex,
    NamedTuple, ClassVar, Union
)

#----------Typings----------
Coord = NewType("coord", NonNegativeInt)
CoordX = NewType("coord_x", Coord)
CoordY = NewType("coord_y", Coord)
CoordZ = NewType("coord_z", Coord)
Width = NewType("width", NonNegativeInt)
Height = NewType("widht", NonNegativeInt)

XY_Tuple = NewType("xy_tuple", Tuple[CoordX, CoordY])
XY_List = NewType("xy_list", List[XY_Tuple])
BoxList = NewType("[x,y,w,h]", List[NonNegativeInt])



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


#class GeomBase(BaseModel, ABC):
#    """ Geometría base."""
#    @abstractmethod
#    def move(*args, **kwargs) -> None: ...


class Point(BaseModel):
    """
    - TODO: Ver si podría implementarse esto con numpy. Sería interesante.
    - FIXME: Ver como se puede encapsular el assert del xy.
    - FIXME: Ver como puedo hacer para que `xy` sea serializado y checkeado todo encapsulado.
    """
    xy: XY_Tuple

    @property
    def x(self) -> CoordX: return self.xy[0]
    @property
    def y(self) -> CoordY: return self.xy[1]

    @staticmethod
    def serial(p: Point | XY_Tuple) -> Point:
        if is_point(p):
            return p
        elif is_xy(p):
            return Point.from_xy(p)
        else:
            raise TypeError("Tipo incorrecto para `Point`.")
    
    @staticmethod
    def from_xy(xy: XY_Tuple) -> Point:
        return Point(xy=xy)
    
    def move(self, xy: XY_Tuple) -> None:
        assert_xy(xy)
        self.xy = xy
    
    def __eq__(self, other: Point) -> bool:
        return self.xy == other.xy
    #def __add__(self, other: CoordXY) -> CoordXY:
    #TODO: todas las operaciones



P_List = NewType("List[Point]", List[Point])

class PointList(MutableSequence, BaseModel):
    """
    Lista de puntos, se comporta igual que una lista, con el agregado
    que solo puede almacenar objetos de tipo `Point`.
    - FIXME: Ver una manera copada de serializar los point que entran en los metodos.
    - FIXME: Ver también la referencia a los objetos, si se copian o no.
    - FIXME: Pensar como puedo hacer que el usuario pueda generar restriscciones
    personalizadas a lo que se almacena dentro de data. Por ejemplo, un rectángulo tiene 4 puntos, etc...
    """
    p_list: P_List = Field(frozen=True)

    @validator("p_list", pre=True, each_item=True)
    def _point_serializer(cls, point: Point | XY_Tuple) -> Point:
        """ BUG: @validator, está deprecado, investigar `field_serializer`."""
        return Point.serial(point)
    
    ########## Modify Points Stored ##########
    def clear(self) -> None: return self.data.clear()

    def pop(self, index: SupportsIndex) -> Point:
        return self.p_list.pop(index)

    def insert(self, index: SupportsIndex, point: Point | XY_Tuple) -> None:
        self.p_list.insert(index, Point.serial(point))

    def __getitem__(self, index: SupportsIndex | slice) -> Point | P_List:
        return self.p_list.__getitem__(index)

    @dispatch(SupportsIndex, tuple)
    def __setitem__(self, index: SupportsIndex, xy: XY_Tuple) -> None:
        self.p_list.__setitem__(index, Point.from_xy(xy))
    
    @dispatch(SupportsIndex, Point)
    def __setitem__(self, index: SupportsIndex, point: Point) -> None:
        self.p_list.__setitem__(index, point)

    @dispatch(slice, Iterable)
    def __setitem__(self, index: slice, p_list: Iterable) -> None:
        self.p_list.__setitem__(index, [Point.serial(p) for p in p_list])
    ########## Modify Points Stored ##########


    def __len__(self) -> int: return self.p_list.__len__()
    def __str__(self) -> str: return self.p_list.__str__()
    def __repr__(self) -> str: return self.p_list.__repr__()
    def __delitem__(self, index: SupportsIndex | slice) -> None:
        self.p_list.__delitem__(index)



#class Area(PointList):     # El último conecta con el primero. También hay que ver como chequear si las lineas se cortan.
#class Polygon(Area):


class Box(BaseModel):
    """
    - (x2, y2) = (x1+w, y1+h)
    - xy_tl=(x1,y1) +--------+ xy_tr=(x2,y1)
    - xy_bl=(x1,y2) +--------+ xy_br=(x2,y2)
    """
    box: BoxList

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


























# bbox, hex, triangle, ....