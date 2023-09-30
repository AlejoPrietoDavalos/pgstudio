__all__ = [
    "Coord", "CoordX", "CoordY",
    "XY_Tuple", "Width", "Height"
]

from . import shp

import numpy as np

from typing import TypeVar, NewType, Tuple

Coord = NewType("coord", np.number)
CoordX = NewType("coord_x", Coord)
CoordY = NewType("coord_y", Coord)
CoordXY = NewType("coord_xy", np.ndarray)   # shape: 1x2
CoordsXY = NewType("coords_xy", np.ndarray) # shape: Nx2


XY_Tuple = NewType("xy", Tuple[float, float])

Width = NewType("width", np.number)
Height = NewType("height", np.number)

T_Geometry = TypeVar("T_Geometry", bound=shp.base.BaseGeometry)
