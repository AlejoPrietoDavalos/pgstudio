from pygameapp.ui.abc import Drawable

from abc import ABC, abstractmethod

import pygame as pg

from typing import NewType

BtnName = NewType("btn_name", str)


class Widget(Drawable, ABC):
    pass


class BtnRectBase(Widget, ABC):
    @abstractmethod
    def draw(self):
        """ Dibuja al botón."""
        ...


class Rect(ABC):
    pass


class BtnsScene():
    pass
