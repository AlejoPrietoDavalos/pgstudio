from pygameapp.window import Drawable

from abc import ABC, abstractmethod

import pygame as pg

from typing import NewType

BtnName = NewType("btn_name", str)

class BtnRectBase(Drawable, ABC):
    @abstractmethod
    def draw(self):
        """ Dibuja al botón."""
        ...
    

class Rect(ABC):
    pass

class BtnsScene():
    pass
