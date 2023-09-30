from __future__ import annotations
__all__ = ["Point"]

from . import shp
from .abc import ShpGeomBase

from .typings import T_Geometry, CoordX, CoordY, XY_Tuple
from typing import TypeVar


T_Point = TypeVar("T_Point", bound="Point")

class Point(ShpGeomBase[shp.Point]):
    def __init__(self, pt_geom: T_Geometry): #, zorder: int
        super().__init__(geom=pt_geom)
    
    @property
    def x(self) -> CoordX:
        return self.geom.x
    
    @property
    def y(self) -> CoordY:
        return self.geom.y
    
    @property
    def xy(self) -> XY_Tuple:
        return self.x, self.y
    
    def __add__(self, pt: T_Point) -> T_Point:
        return Point(shp.Point(self.coords + pt.coords))

    def __sub__(self, pt: T_Point) -> T_Point:
        return Point(shp.Point(self.coords - pt.coords))
