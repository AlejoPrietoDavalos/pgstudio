from abc import ABC, abstractmethod

from pgstudio.display import Window, T_WinRes

import pygame as pg


#from enum import Enum
#class StateApp(Enum):
#    IS_RUNNING
#    PLAYING


class PyGameApp(ABC):
    def __init__(self, app_name: str, resolution: T_WinRes, fps: int):
        pg.init()
        self._is_running = True
        self.window = Window(
            app_name = app_name,
            resolution = resolution,
            fps = fps
        )
    
    #@property
    #def win(self) -> pg.Surface:
    #    """ FIXME: Hace falta??."""
    #    return Window.win

    @property
    def is_running(self) -> bool:
        return self._is_running
    
    @abstractmethod
    def run_app(self) -> None:
        """ TODO: Poner docstring."""
        ...
