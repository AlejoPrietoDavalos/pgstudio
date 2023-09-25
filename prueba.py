""" Geometrías para almacenar datos geométricos."""
from __future__ import annotations

from pydantic import BaseModel, NonNegativeInt, Field
from pydantic import validate_call

from typing import NewType, Tuple, List

#----------Typings----------
Coord = NewType("coord", NonNegativeInt)
CoordX = NewType("x", Coord)
CoordY = NewType("y", Coord)
CoordZ = NewType("z", Coord)
XY_Tuple = NewType("(x,y)", Tuple[CoordX, CoordY])
XY_List = NewType("list[(x,y), ...)]", List[XY_Tuple])


class Point(BaseModel):
    x: CoordX
    y: CoordY

    @property
    def xy(self) -> XY_Tuple:
        return self.x, self.y

    def update(self, xy: XY_Tuple) -> None:
        self.x, self.y = xy

    @staticmethod
    def from_xy(xy: XY_Tuple) -> Point:
        x, y = xy
        return Point(x=x, y=y)
p = Point(x=3,y=2)
print(p)