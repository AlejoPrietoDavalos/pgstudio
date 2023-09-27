import numpy as np

from typing import NewType, Tuple

#----------Coords----------
Coord = NewType("coord", np.number)
Coords = NewType("arr_1d", np.ndarray[Coord])

CoordX = NewType("coord_x", np.number)
CoordY = NewType("coord_y", np.number)
CoordXY = NewType("xy_arr", np.ndarray[np.shape((2,)), np.number])

XY_Tuple = NewType("xy", Tuple[np.number, np.number])


#----------Distances----------
#DistPix = NewType("pix", np.number)     # Ver como convertir a No-Negativo.
#Width = NewType("width", np.number)     # Ver como convertir a No-Negativo.
#Height = NewType("widht", np.number)    # Ver como convertir a No-Negativo.

# Estructuras.
#XY_Tuple = NewType("xy_tuple", Tuple[CoordX, CoordY])
#XY_List = NewType("xy_list", List[XY_Tuple])
#BoxList = NewType("[x1,y1,w,h]", List[NonNegativeInt])