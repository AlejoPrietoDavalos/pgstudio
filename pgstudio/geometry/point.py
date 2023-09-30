from __future__ import annotations
__all__ = ["Point"]

from . import shp

from typing import TypeVar



T_Point = TypeVar("T_Point", bound="Point")

class Point:
    def __init__(self, shp_point: shp.Point): #, zorder: int
        self._shp_point: shp.Point = shp_point

    @property
    def shp_point(self) -> shp.Point:
        return self._shp_point
    
    @shp_point.setter
    def shp_point(self, p: shp.Point) -> None:
        assert isinstance(p, shp.Point)
        self._shp_point = p

    def __str__(self) -> str: return self.arr.__str__()
    def __repr__(self) -> str: return self.arr.__repr__()

    def __add__(self, p: T_Point) -> T_Point: return self.create(self.arr + v.arr)
    def __sub__(self, p: T_Point) -> T_Point: return self.create(self.arr - v.arr)
    def __mul__(self, p: T_Point) -> T_Point: return self.create(self.arr * v.arr)
    def __div__(self, p: T_Point) -> T_Point: return self.create(self.arr / v.arr)
