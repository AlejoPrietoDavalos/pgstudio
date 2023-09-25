"""
Modelo de pkmn, ver lo más genérico posible,
y los casos particulares después se retocan.
"""
from pydantic import BaseModel


class Pkmn(BaseModel):
    id: int
    tipo_1: str
    tipo_2: str
    #etc...



