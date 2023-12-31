""" Módulo para controlar las geometrías del juego. Por lo pronto se usará `shapely`."""
import shapely.geometry as shp

from .typings import *
from .abc import *

from .point import *
from .linestring import *
from .polygon import *
from .box import *
