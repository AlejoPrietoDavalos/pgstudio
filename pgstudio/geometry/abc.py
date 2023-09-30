from __future__ import annotations
__all__ = []

from . import shp

from abc import ABC, abstractproperty, abstractmethod

from .typings import T_Geometry, CoordXY, CoordsXY
from typing import Generic


#class GeomBase(ABC):
#    """ Esta sería la base de todas las geometrías."""
#    pass



class ShpGeomBase(Generic[T_Geometry], ABC):
    def __init__(self, geom: T_Geometry):
        assert isinstance(geom, shp.base.BaseGeometry)
        self._geom = geom
    
    @property
    def geom(self) -> T_Geometry:
        return self._geom
    
    @geom.setter
    def geom(self, new_geom: T_Geometry) -> None:
        #assert isinstance(new_geom, shp.Point)
        self._geom = new_geom

    @property
    def coords(self) -> CoordXY | CoordsXY:
        return self.geom.coords.__array__(dtype=None)

    def __str__(self) -> str: return str(self.geom)
    def __repr__(self) -> str: return repr(self.geom)
    
    def __eq__(self, other: T_Geometry) -> bool:
        return self.geom == other.geom

    #@abstractmethod
    #def move(self, pt: T_Point) -> None: ...

