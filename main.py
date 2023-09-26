import pygame as pg

from emolgapp.scenes.main_menu import MainMenu
from pgstudio.app import PyGameApp

import pygame as pg


from typing import NewType, Tuple, NamedTuple
from pgstudio.geometry.typings import Width, Height


class WidthHeight(NamedTuple):
    w: Width
    h: Height


class EmolgApp(PyGameApp):
    def __init__(self, app_name: str, resolution: WidthHeight):
        super().__init__(app_name, resolution)
    
    def run_app(self) -> None:
        scene = MainMenu()
        scene.main_loop()



pgapp = EmolgApp(
    app_name = "EmolgApp",
    resolution = WidthHeight(800, 600)
)

pgapp.run_app()
