from __future__ import annotations
from abc import ABC, abstractmethod
from functools import cached_property
import attr

import pygame as pg

from typing import Dict

class PygameApp:
    pass

class EmolgApp(PygameApp):
    pass
pg.init()
pg.display.set_caption("EmolgApp Online")

class Validations:
    pass


@attr.s
class Scene:
    
    def main_loop(self):
        pass

class Scenes(Dict[str, Scene]):
    """
    - TODO: Si no deleteo la Scena como key-value, seestá guardando la
    información de la escena. Y se podría volver,sería como una especie de 'cache'.
    - TODO: También recordar como definir el __getitem__ y __setitem__, que cree las escenas.
    """
    def add_scene():
        pass

class Widget:
    pass





