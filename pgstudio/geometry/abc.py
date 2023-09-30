from __future__ import annotations
__all__ = []

from . import shp

from abc import ABC, abstractproperty

from .typings import CoordX, CoordY, CoordXY, XY_Tuple
from typing import TypeVar


T_ShpGeomBase = TypeVar("T_ShpGeomBase", bound="ShpGeomBase")

#class GeomBase(ABC):
#    """ Esta sería la base de todas las geometrías."""
#    pass


class ShpGeomBase(ABC):
    def __init__(self, geom: shp.base.BaseGeometry):
        assert isinstance(geom, shp.base.BaseGeometry)
        self._geom = geom
    
    @abstractproperty
    def geom(self) -> shp.base.BaseGeometry: ...
    
    @abstractproperty
    @geom.setter
    def geom(self, new_geom: shp.base.BaseGeometry) -> None: ...

    def __str__(self) -> str: return str(self.geom)
    def __repr__(self) -> str: return repr(self.geom)
    
    def __eq__(self, other: T_ShpGeomBase) -> bool:
        return self.geom == other.geom

    #@abstractmethod
    #def move(self, pt: T_Point) -> None: ...


T_PointBase = TypeVar("T_PointBase", bound="PointBase")

class PointBase(ShpGeomBase, ABC):
    def __init__(self, pt_geom: shp.Point): #, zorder: int
        super().__init__(geom=pt_geom)
    
    @property
    def geom(self) -> shp.Point:
        return self._geom
    
    @geom.setter
    def geom(self, new_pt_geom: shp.Point) -> None:
        assert isinstance(new_pt_geom, shp.Point)
        self._geom = new_pt_geom

    @property
    def coords(self) -> CoordXY:
        return self.geom.coords.__array__()
    
    @property
    def x(self) -> CoordX:
        return self.geom.x
    
    @property
    def y(self) -> CoordY:
        return self.geom.y
    
    @property
    def xy(self) -> XY_Tuple:
        return self.x, self.y
    
    def __add__(self, pt: T_PointBase) -> T_PointBase:
        return PointBase(shp.Point(self.coords + pt.coords))

    def __sub__(self, pt: T_PointBase) -> T_PointBase:
        return PointBase(shp.Point(self.coords - pt.coords))


class LineStringBase(ShpGeomBase, ABC):
    #shp.LineString
    pass


class PolygonBase(ShpGeomBase, ABC):
    pass


class BoxBase(ShpGeomBase, ABC):
    pass
