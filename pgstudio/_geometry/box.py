from __future__ import annotations
__all__ = ["Box"]

from .np_array import ArrNP

import numpy as np

from abc import ABC

from .typings import CoordX, CoordY, Width, Height, BoxList, XY_Tuple, BoxArr




class BoxBase(ArrNP, ABC):
    def __init__(self, arr: BoxArr, dtype: np.dtype = None):
        super().__init__(arr=arr, dtype=dtype)

    @property
    def arr(self) -> BoxArr:
        return self._arr
    
    @arr.setter
    def arr(self, arr: BoxArr) -> None:
        assert len(arr)
        self._arr = None

class Box(BoxBase):
    """
    - box (np.ndarray[x1, y1, w, h])

    - (x2, y2) = (x1+w, y1+h)
    - xy_tl=(x1,y1) +--------+ xy_tr=(x2,y1)
    - xy_bl=(x1,y2) +--------+ xy_br=(x2,y2)
    """
    def __init__(self, arr: BoxArr, dtype: np.dtype = None):
        super().__init__(arr=arr, dtype=dtype)
    
    #-----> `xy_ref` de referencia.
    @property
    def xy_ref(self) -> XY_Tuple:
        return self.xy_tl

    @property
    def x1(self) -> CoordX: return self.arr[0]
    @property
    def y1(self) -> CoordY: return self.arr[1]
    @property
    def w(self) -> Width: return self.arr[2]
    @property
    def h(self) -> Height: return self.arr[3]
    @property
    def x2(self) -> CoordX: return self.x1 + self.w
    @property
    def y2(self) -> CoordY: return self.y1 + self.h

    #-----> `XY_Tuple` de las 4 esquinas del rectángulo.
    @property
    def xy_tl(self) -> XY_Tuple: return self.x1, self.y1
    @property
    def xy_tr(self) -> XY_Tuple: return self.x2, self.y1
    @property
    def xy_br(self) -> XY_Tuple: return self.x2, self.y2
    @property
    def xy_bl(self) -> XY_Tuple: return self.x1, self.y2

    #-----> `Point` de las 4 esquinas del rectángulo.
    # @property
    # def p_tl(self) -> Point: return Point(xy=self.xy_tl)
    # @property
    # def p_tr(self) -> Point: return Point(xy=self.xy_tr)
    # @property
    # def p_br(self) -> Point: return Point(xy=self.xy_br)
    # @property
    # def p_bl(self) -> Point: return Point(xy=self.xy_bl)

    #def intersects(self, point: XY_Tuple | Point) -> bool:
    #    """ True si el punto se encuentra dentro."""
    #    point = Point.serial(point)
    #    return (self.x1 <= point.x <= self.x2) and \
    #           (self.y1 <= point.y <= self.y2)

    def translation(self, v) -> None:
        # FIXME: POner un vector despues.
        dx, dy = v
        self._box[0] += dx
        self._box[1] += dy

    def move(self, xy: XY_Tuple) -> None:
        self._box[0], self._box[1] = xy