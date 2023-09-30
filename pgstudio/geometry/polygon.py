from __future__ import annotations
__all__ = ["Polygon"]

from . import shp

from .abc import ShpGeomBase

from .typings import T_Geometry, CoordsXY

class Polygon(ShpGeomBase[shp.Polygon]):
    def __init__(self, pol_geom: T_Geometry):
        super().__init__(geom=pol_geom)

    @property
    def coords(self) -> CoordsXY:
        return self.geom.exterior.coords.__array__(dtype=None)