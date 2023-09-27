from __future__ import annotations
from pgstudio.geometry import Coord

#def is_vector(v: VectorRn) -> bool: return isinstance(v, VectorRn)  # TODO: Probar con el TypeVar, a ver si funciona.
#def assert_vector(v: VectorRn) -> None: assert is_vector(v)
from pgstudio.geometry import VectorR2

import numpy as np

v1 = VectorR2(np.array([2,1]), dtype=np.int16)
v2 = VectorR2(np.array([3,4]), dtype=np.int16)
v3 = v1 + v2
print("------")
print(v1.x)
print(v1.y)
print(v1.xy)
print(v1.xy_ref)
print(v1.dtype)
print(v1)
v1.move(v2)
print(v1)
print()
print()
print()





