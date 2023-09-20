from abc import ABC, abstractmethod
from pygameapp.window import Window

import pygame as pg

from emolgapp.scenes import MainMenu
from pygameapp.app import PyGameApp

import pygame as pg



class EmolgApp(PyGameApp):
    def __init__(self, app_name: str, resolution: tuple[int, int]):
        super().__init__(app_name, resolution)
    
    def run_app(self) -> None:
        scene = MainMenu()
        #while self.is_running:
        #    scene.main_loop()
        scene.main_loop()
    


pgapp = EmolgApp(
    "EmolgApp",
    (800, 600)
)

pgapp.run_app()
