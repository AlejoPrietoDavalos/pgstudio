from abc import ABC, abstractmethod

from pgstudio.window import Window
import pygame as pg

class PyGameApp(ABC):
    def __init__(self, app_name: str, resolution: tuple[int, int]):
        pg.init()
        pg.display.set_caption(app_name)
        Window.set_win(resolution=resolution)
        self._is_running = True
    
    @property
    def is_running(self) -> bool:
        return self._is_running
    
    @abstractmethod
    def run_app(self) -> None:
        ...