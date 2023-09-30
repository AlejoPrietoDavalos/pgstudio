from __future__ import annotations

from . import shp

from .abc import PointBase


class Point(PointBase):
    def __init__(self, pt_geom: shp.Point):
        super().__init__(pt_geom=pt_geom)

