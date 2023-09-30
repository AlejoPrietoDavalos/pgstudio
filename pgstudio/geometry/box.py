from __future__ import annotations
__all__ = ["Box"]

from .point import Point
from .polygon import Polygon

from abc import ABC

import numpy as np

from .typings import Width, Height


class Box(Polygon, ABC):
    def __init__(self, pt_geom: Point, w: Width, h: Height):
        pass