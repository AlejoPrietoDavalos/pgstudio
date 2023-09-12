from __future__ import annotations
from abc import ABC, abstractmethod
from functools import cached_property
import attr

import pygame as pg

from typing import Dict

class PygameApp:
    def __init__(
            self,
            app_name: str):
        pg.init()
        pg.display.set_caption(app_name)



class EmolgApp(PygameApp):
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


# -----Revisar
class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()







pgapp = PygameApp("EmolgApp")





