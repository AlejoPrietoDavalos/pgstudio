from __future__ import annotations

from pydantic import BaseModel, PositiveInt

from typing import NewType, Tuple

#----------Typings----------
Coord = NewType("coord", PositiveInt)
CoordX = NewType("x", Coord)
CoordY = NewType("y", Coord)
CoordZ = NewType("z", Coord)
XY_Tuple = NewType("(x,y)", Tuple[CoordX, CoordY])


class PointXY(BaseModel):
    x: CoordX
    y: CoordY

    @property
    def xy(self) -> XY_Tuple:
        return self.x, self.y

    @staticmethod
    def from_xy(xy: XY_Tuple) -> PointXY:
        return PointXY(x=xy[0], y=xy[1])


