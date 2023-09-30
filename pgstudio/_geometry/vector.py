from __future__ import annotations
__all__ = ["VectorR2"]

from .np_array import ArrNP
import numpy as np

from abc import ABC

from typing import TypeVar, Type
from .typings import CoordX, CoordY, CoordXY, Coords, XY_Tuple



#T_VectorNP = TypeVar("T_VectorNP", bound="VectorNP")

class VectorNP(ArrNP):
    """ Funcionalidades heredadas de Numpy."""
    def __init__(self, arr: Coords, dtype: np.dtype = None):
        assert len(arr.shape) == 1, "Un vector tiene dimensión 1."
        super().__init__(arr=arr, dtype=dtype)
    
    @property
    def arr(self) -> Coords:
        """ Coordenadas del vector."""
        return self._arr

    @arr.setter
    def arr(self, new_arr: Coords) -> None:
        isinstance(new_arr, np.ndarray)
        self._arr = np.array(new_arr)



T_VectorRn = TypeVar("T_VectorRn", bound="VectorRn")

class VectorRn(VectorNP):
    def translation(self, v: T_VectorRn) -> None:
        self.arr += v.arr

    def move(self, v: T_VectorRn) -> None:
        self.arr = v.arr


class VectorR2Base(VectorRn, ABC):
    def __init__(self, arr: CoordXY, dtype: np.dtype = None):
        assert len(arr) == 2
        super().__init__(arr=arr, dtype=dtype)
    
    @property
    def arr(self) -> CoordXY:
        return super().arr
    
    @arr.setter
    def arr(self, new_arr: CoordXY) -> None:
        assert len(new_arr) == 2
        self._arr = np.array(new_arr, dtype=self.dtype)
    
    # ~~~~> Coords xy
    @property
    def x(self) -> CoordX: return self.arr[0]
    @x.setter
    def x(self, x_: CoordX) -> None: self.arr[0] = x_
    @property
    def y(self) -> CoordY: return self.arr[1]
    @x.setter
    def y(self, y_: CoordY) -> None: self.arr[1] = y_
    @property
    def xy(self) -> XY_Tuple: return self.x, self.y
    @property
    def xy_ref(self) -> XY_Tuple: return self.xy


class VectorR2(VectorR2Base):
    def __init__(self, arr: CoordXY, dtype: np.dtype = None):
        super().__init__(arr=arr, dtype=dtype)
