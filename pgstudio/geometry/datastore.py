""" Geometrías para almacenar datos geométricos."""
from __future__ import annotations

from pydantic import BaseModel, NonNegativeInt, field_validator, Field
from multipledispatch import dispatch

from collections.abc import Iterator, MutableSequence, Iterable
#from abc import ABC, abstractmethod

from typing import (
    NewType, Tuple, List, SupportsIndex,
    NamedTuple, ClassVar, Union
)

#----------Typings----------
Coord = NewType("coord", NonNegativeInt)
CoordX = NewType("coord_x", Coord)
CoordY = NewType("coord_y", Coord)
CoordZ = NewType("coord_z", Coord)
XY_Tuple = NewType("xy_tuple", Tuple[CoordX, CoordY])
XY_ListOfTuples = NewType("xy_list_of_tuples", List[XY_Tuple])


def is_xy(xy: XY_Tuple) -> bool:
    return isinstance(xy, tuple) and len(xy)==2 and \
       all(isinstance(c, int) for c in xy)

def is_point(point: Point) -> bool:
    return isinstance(point, Point)

def assert_xy(xy: XY_Tuple) -> None:
    assert is_xy(xy)

def assert_xy_list_of_tuples(xy_list_of_tuples: XY_ListOfTuples) -> None:
    assert isinstance(xy_list_of_tuples, list)
    assert all(is_xy(xy) for xy in xy_list_of_tuples)



class CoordXY(BaseModel):
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

    def move(self, xy: XY_Tuple) -> None:
        assert_xy(xy)
        self.xy = xy
    
    def __eq__(self, other: Point) -> bool:
        return self.xy == other.xy
    #def __add__(self, other: CoordXY) -> CoordXY:
    #TODO: todas las operaciones



class Point(CoordXY):
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



# typing
PList = NewType("List[Point]", List[Point])

class PointList(MutableSequence, BaseModel):
    """
    Lista de puntos, se comporta igual que una lista, con el agregado
    que solo puede almacenar objetos de tipo `Point`.
    - FIXME: Ver una manera copada de serializar los point que entran en los metodos.
    - FIXME: Ver también la referencia a los objetos, si se copian o no.
    """
    data: PList = Field(frozen=True)
    
    #@field_validator('data', pre=True, each_item=True)
    #def _point_serializer(cls, point: Point | XY_Tuple) -> Point:
    #    return Point.serial(point)
    
    
    ########## Modify Points Stored ##########
    def clear(self) -> None: return self.data.clear()

    def pop(self, index: SupportsIndex) -> Point:
        return self.data.pop(index)

    def insert(self, index: SupportsIndex, point: Point | XY_Tuple) -> None:
        self.data.insert(index, Point.serial(point))

    def __getitem__(self, index: SupportsIndex | slice) -> Point | PList:
        return self.data.__getitem__(index)

    @dispatch(SupportsIndex, tuple)
    def __setitem__(self, index: SupportsIndex, xy: XY_Tuple) -> None:
        self.data.__setitem__(index, Point.from_xy(xy))
    
    @dispatch(SupportsIndex, Point)
    def __setitem__(self, index: SupportsIndex, point: Point) -> None:
        self.data.__setitem__(index, point)

    @dispatch(slice, Iterable)
    def __setitem__(self, index: slice, p_list: Iterable) -> None:
        self.data.__setitem__(index, [Point.serial(p) for p in p_list])
    ########## Modify Points Stored ##########


    def __len__(self) -> int: return self.data.__len__()
    def __str__(self) -> str: return self.data.__str__()
    def __repr__(self) -> str: return self.data.__repr__()
    def __delitem__(self, index: SupportsIndex | slice) -> None:
        self.data.__delitem__(index)



class Polygon(PointList):
    pass

# bbox, hex, triangle, ....