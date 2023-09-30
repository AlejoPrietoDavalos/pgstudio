from __future__ import annotations
__all__ = ["LineString"]

from . import shp

from .abc import ShpGeomBase

from .typings import T_Geometry

class LineString(ShpGeomBase[shp.LineString]):
    def __init__(self, line_geom: T_Geometry):
        super().__init__(geom=line_geom)
