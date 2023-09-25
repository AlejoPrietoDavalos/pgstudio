from pydantic import NonNegativeInt

from typing import NewType, Tuple, List

#----------Typings----------
# Coordenadas.
Coord = NewType("coord", NonNegativeInt)
CoordX = NewType("coord_x", Coord)
CoordY = NewType("coord_y", Coord)
CoordZ = NewType("coord_z", Coord)

# Dimenciones.
DistPix = NewType("pix", NonNegativeInt)
Width = NewType("width", DistPix)
Height = NewType("widht", DistPix)

# Estructuras.
XY_Tuple = NewType("xy_tuple", Tuple[CoordX, CoordY])
XY_List = NewType("xy_list", List[XY_Tuple])
BoxList = NewType("[x1,y1,w,h]", List[NonNegativeInt])