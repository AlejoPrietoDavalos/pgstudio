from __future__ import annotations
__all__ = ["ArrNP"]

#from abc import ABC

import numpy as np

from typing import TypeVar, Type


T_ArrNP = TypeVar("T_ArrNP", bound="ArrNP")

class ArrNP:
    def __init__(self, arr: np.ndarray, dtype: np.dtype = None):
        self._arr: np.ndarray = np.array(arr, dtype=dtype)
    
    @classmethod
    def create(cls: Type[T_ArrNP], arr: np.ndarray, dtype: np.dtype = None) -> T_ArrNP:
        """ Crea una nueva instancia de array."""
        return cls(arr, dtype)
    
    @property
    def arr(self) -> np.ndarray:
        return self._arr
    
    @arr.setter
    def arr(self, new_arr: np.ndarray) -> None:
        isinstance(new_arr, np.ndarray)
        self._arr = np.array(new_arr)

    @property
    def dtype(self) -> np.dtype:
        return self.arr.dtype
    
    @property
    def dim(self) -> int:
        return len(self.arr)

    def __str__(self) -> str: return self.arr.__str__()
    def __repr__(self) -> str: return self.arr.__repr__()

    def __add__(self, v: T_ArrNP) -> T_ArrNP: return self.create(self.arr + v.arr)
    def __sub__(self, v: T_ArrNP) -> T_ArrNP: return self.create(self.arr - v.arr)
    def __mul__(self, v: T_ArrNP) -> T_ArrNP: return self.create(self.arr * v.arr)
    def __div__(self, v: T_ArrNP) -> T_ArrNP: return self.create(self.arr / v.arr)
    
    # TODO: TESTEAR
    def __eq__(self, v: T_ArrNP) -> bool: return self.arr == v.arr


