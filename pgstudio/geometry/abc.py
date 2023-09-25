""" ABC para la geometría."""
from __future__ import annotations

from pydantic import BaseModel

from abc import ABC, abstractmethod, abstractproperty

from pgstudio.geometry.typings import XY_Tuple

from typing import NewType, Tuple
Vector = NewType("vector", Tuple[int, int])

class GeomBase(BaseModel, ABC):
    """
    Implementar:
    - xy_ref (property): Punto de referencia del objeto geométrico.
    - move (method): Traslada al objeto entero del `xy_ref` al punto `xy`.
    - translation (method): Traslada al objeto entero del `xy_ref` en
    dirección al vector `v`.
    """
    # FIXME: Poner un vector como input, crear la clase.
    # Ver como desagregar de Point, que sean cosas distintas pero relacionadas.
    @abstractproperty
    def xy_ref(self) -> XY_Tuple: ...
    # TODO: Ver de agregar p_ref que devuelva un Point.
    @abstractmethod
    def translation(self, v: Vector) -> None: ...
    # IDEA: Puede serializar el input a un vector. Y haga los calculos.
    @abstractmethod
    def move(self, xy: XY_Tuple) -> None: ...


# TODO
#class CoordXY(BaseModel, ABC):
#    pass
#class Vector(CoordXY):