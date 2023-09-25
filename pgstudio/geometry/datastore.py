""" Geometrías para almacenar datos geométricos."""
from __future__ import annotations

from pydantic import BaseModel, NonNegativeInt, validator
from multipledispatch import dispatch

from collections.abc import MutableSequence, Iterable

from typing import NewType, Tuple, List, SupportsIndex, NamedTuple, ClassVar

#----------Typings----------
Coord = NewType("coord", NonNegativeInt)
CoordX = NewType("coord_x", Coord)
CoordY = NewType("coord_y", Coord)
CoordZ = NewType("coord_z", Coord)
XY_Tuple = NewType("xy_tuple", Tuple[CoordX, CoordY])
XY_ListOfTuples = NewType("xy_list_of_tuples", List[XY_Tuple])

def assert_xy(xy: XY_Tuple) -> None:
    assert isinstance(xy, tuple) and len(xy)==2, "xy es una tupla de 2 coordenadas."
    assert all(isinstance(_c, int) and _c>=0 for _c in xy), "xy es entero positivo."

def assert_xy_list(xy_list: XY_List) -> None:
    assert isinstance(xy_list, list) and \
       all(isinstance(xy, tuple) for xy in xy_list)



class CoordXY(BaseModel):
    """
    - TODO: Ver si podría implementarse esto con numpy. Sería interesante.
    - FIXME: Ver como se puede encapsular el assert del xy.
    """
    xy: XY_Tuple

    @property
    def x(self) -> CoordX: return self.xy[0]
    @property
    def y(self) -> CoordY: return self.xy[1]

    def move(self, xy: XY_Tuple) -> None:
        assert_xy(xy)
        self.xy = xy
    
    #def __add__(self, other: CoordXY) -> CoordXY:
    #TODO: todas las operaciones



class Point(CoordXY):
    pass



# typing
XY_List = NewType("xy_list", List[CoordXY])
PList = NewType("List[Point]", List[Point])

class PointList(MutableSequence, BaseModel):
    p_list: PList

    @staticmethod
    def from_xy_list(xy_list: XY_List) -> PointList:
        assert_xy_list(xy_list=xy_list)
        return PointList(p_list=[Point.from_xy(xy) for xy in xy_list])

    def __getitem__(self, index: SupportsIndex | slice) -> Point | PList:
        return self.p_list.__getitem__(index)

    @dispatch(SupportsIndex, Point)
    def __setitem__(self, index: SupportsIndex, point: Point) -> None:
        self.p_list.__setitem__(index, point)
    
    @dispatch(slice, Iterable)
    def __setitem__(self, index: slice, p_list: Iterable) -> None:
        assert all(isinstance(p, Point) for p in p_list)
        self.p_list.__setitem__(index, p_list)
    
    def insert(self, index: SupportsIndex, point: Point) -> None:
        assert isinstance(point, Point)
        self.p_list.insert(index, point)
    
    def __len__(self) -> int:
        return len(self.p_list)
    
    def __delitem__(self, index: SupportsIndex | slice) -> None:
        del self.p_list[index]
    
    def __repr__(self) -> str:
        return repr(self.p_list)



class Polygon(PointList):
    pass

# bbox, hex, triangle, ....