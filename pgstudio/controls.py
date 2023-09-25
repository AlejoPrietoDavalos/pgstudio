from pgstudio.geometry.datastore import Point, XY_Tuple

import pygame as pg

from abc import ABC, abstractmethod

from typing import Tuple

class MousePos(Point):
    def __init__(self, xy: XY_Tuple):
        super().__init__(xy=xy)
    
    def update(self) -> None:
        """ Recalcula la posición actual del mouse."""
        self.x, self.y = self._get_mouse_pos()

    @staticmethod
    def _get_mouse_pos() -> XY_Tuple:
        return pg.mouse.get_pos()

class Mouse:
    """ """
    _instance = None
    _instanciated = False
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Mouse, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._instanciated:
            self._instanciated = True
            self.__pos = MousePos(x=0, y=0)

    @property
    def pos(self) -> MousePos: return self.__pos
    @property
    def xy(self) -> XY_Tuple: return self.pos.xy

    def update_pos(self) -> None:
        self.pos.update()




class CtrlsBase(ABC):
    def __init__(self):
        self.mouse = Mouse()

    @abstractmethod
    def update(self):
        """ Actualiza los controles que fueron pulsados."""
        ...