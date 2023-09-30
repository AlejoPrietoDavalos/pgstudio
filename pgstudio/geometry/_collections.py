from __future__ import annotations
__all__ = []

from pgstudio.geometry._datastore import Point, XY_Tuple

from collections.abc import MutableSequence, Iterable

from pydantic import BaseModel, Field, validator
from multipledispatch import dispatch

from typing import NewType, List, SupportsIndex


P_List = NewType("List[Point]", List[Point])

class PointList(MutableSequence, BaseModel):
    """
    Lista de puntos, se comporta igual que una lista, con el agregado
    que solo puede almacenar objetos de tipo `Point`.
    - FIXME: Ver una manera copada de serializar los point que entran en los metodos.
    - FIXME: Ver también la referencia a los objetos, si se copian o no.
    - FIXME: Pensar como puedo hacer que el usuario pueda generar restriscciones
    personalizadas a lo que se almacena dentro de data. Por ejemplo, un rectángulo tiene 4 puntos, etc...
    """
    p_list: P_List = Field(frozen=True)

    def __init__(self, p_list: P_List):
        super().__init__(p_list=p_list)
    
    @validator("p_list", pre=True, each_item=True)
    def _point_serializer(cls, point: Point | XY_Tuple) -> Point:
        """ BUG: @validator, está deprecado, investigar `field_serializer`."""
        return Point.serial(point)
    
    ########## Modify Points Stored ##########
    def clear(self) -> None: return self.p_list.clear()

    def pop(self, index: SupportsIndex) -> Point:
        return self.p_list.pop(index)

    def insert(self, index: SupportsIndex, point: Point | XY_Tuple) -> None:
        self.p_list.insert(index, Point.serial(point))

    def __getitem__(self, index: SupportsIndex | slice) -> Point | P_List:
        return self.p_list.__getitem__(index)

    @dispatch(SupportsIndex, tuple)
    def __setitem__(self, index: SupportsIndex, xy: XY_Tuple) -> None:
        self.p_list.__setitem__(index, Point(xy))
    
    @dispatch(SupportsIndex, Point)
    def __setitem__(self, index: SupportsIndex, point: Point) -> None:
        self.p_list.__setitem__(index, point)

    @dispatch(slice, Iterable)
    def __setitem__(self, index: slice, p_list: Iterable) -> None:
        self.p_list.__setitem__(index, [Point.serial(p) for p in p_list])
    ########## Modify Points Stored ##########


    def __len__(self) -> int: return self.p_list.__len__()
    def __str__(self) -> str: return self.p_list.__str__()
    def __repr__(self) -> str: return self.p_list.__repr__()
    def __delitem__(self, index: SupportsIndex | slice) -> None:
        self.p_list.__delitem__(index)


