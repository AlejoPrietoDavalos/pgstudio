import os
import pygame as pg
from .ctrls import Ctrls
from .buttons import ButtonsContainer
from .utils import Window, FontManager, ColorManager, Wallpaper

class UI():
    def __init__(self):
        self.win = Window()
        self.FPS = 60
        self.CLOCK = pg.time.Clock()
        
        self.FONT = FontManager()
        self.COLOR = ColorManager()
        self.ctrls = Ctrls()
        self.wallpaper = Wallpaper(self.win)
        self.btns = ButtonsContainer()

    def before_changing_scene(self, scene:str):
        self.fill("Black")
        self.wallpaper.set_wallpapers_scene(scene)

    def fill(self, color_name:str):
        """ Rellena toda la pantalla con un color."""
        self.win.fill(self.COLOR.get_color(color_name))
    
    def update_screen(self):
        self.CLOCK.tick(self.FPS)
        pg.display.update()
        self.fill("Black")



