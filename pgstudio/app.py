from abc import ABC, abstractmethod

from pgstudio.display import Window, WinRes

import pygame as pg


#from enum import Enum
#class StateApp(Enum):
#    IS_RUNNING
#    PLAYING


class PyGameApp(ABC):
    def __init__(self, app_name: str, resolution: WinRes):
        pg.init()
        pg.display.set_caption(app_name)

        self._is_running = True
        self.window = Window(resolution=resolution)
    
    @property
    def win(self) -> pg.Surface:
        """ FIXME: Hace falta??."""
        return self.window.win

    @property
    def is_running(self) -> bool:
        return self._is_running
    
    @abstractmethod
    def run_app(self) -> None:
        """ TODO: Poner docstring."""
        ...
