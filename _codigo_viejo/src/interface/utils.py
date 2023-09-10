import pygame as pg
from PIL import Image
import yaml
import os
from typing import Union

from .rcs import _Colors, _Wallpapers

class Resolution():
    """ Son todas resoluciones 16:9."""
    def __init__(self):
        self._active_resolution_name = "1920 x 1080"
        self._RESOLUTIONS = {
            "1920 x 1080":  (1920, 1080),
            "1600 x 900":   (1600, 900),
            "1440 x 810":   (1440, 810),
            "1368 x 768":   (1368, 768),
            "1280 x 720":   (1280, 720),
            "960 x 540":    (960, 540),
            "864 x 486":    (864, 486)
        }
        self._COEF = {r_name: self._RESOLUTIONS[r_name][0]/1920 for r_name in self._RESOLUTIONS}

    def rescale(self, value:Union[dict, int, list]):
        """ Rescala el valor que recibe a la
            resolución que se encuentra activa."""
        if type(value) == dict:
            pass

    def get_active_resolution(self) -> tuple:
        return self._RESOLUTIONS[self._active_resolution_name]


class Window(Resolution):
    def __init__(self):
        super().__init__()
        self._win = pg.display.set_mode(self.get_active_resolution())
    
    def get(self) -> pg.Surface:
        return self._win
    
    def fill(self, color_name:str):
        self._win.fill(color_name)
    
    def blit(self, surface:pg.Surface, coord:tuple):
        self._win.blit(surface, coord)
    
    def change_resolution(self, new_resolution:str):
        """ Se le pasa el string con la clave de la nueva resolución."""
        self.active_resolution = new_resolution
    


class FontManager():
    _BASE_FONT_PATH = os.path.join("src", "interface", "fonts")
    _FONT_ROUTING_PATH = os.path.join(_BASE_FONT_PATH, "font_routing.yaml")

    def __init__(self):
        self.font_path = self._load_font_paths()

    def get_font(self, font_name:str, font_size:int) -> pg.font.Font:
        return pg.font.Font(self.font_path[font_name], font_size)

    def get_text_size(self, font:pg.font.Font, text:str) -> dict:
        """ Width y height del texto dada la font."""
        w_text, h_text = font.size(text)
        return {"w": w_text, "h": h_text}

    def _load_font_paths(self) -> dict:
        """ Devuelve un diccionario con la ruta absoluta de cada fuente dado su nombre como clave.

            Example
            -------
            'font_name': 'absolute_path'"""
        font_path = yaml.load(open(self._FONT_ROUTING_PATH, 'r'), yaml.loader.SafeLoader)
        for key in font_path:
            font_path[key] = os.path.join(self._BASE_FONT_PATH, font_path[key])
        return font_path


class ColorManager(_Colors):
    def __init__(self):
        super().__init__()
    
    def get_color(self, color_name:str) -> tuple:
        return self._COLOR[color_name]


class Wallpaper(_Wallpapers):
    def __init__(self, win:Window):
        self.win = win
        self.active_wallpaper = pg.Surface

    def set_wallpaper(self, wallpaper_name:str):
        img = Image.open(self.wallpapers_path[wallpaper_name]).resize(self.win.get_active_resolution())
        self.active_wallpaper = pg.image.fromstring(img.tobytes(), img.size, img.mode)
        
        #self.active_wallpaper = pg.transform.scale(pg.image.load(self.wallpapers_path[wallpaper_name]).convert(), (1920,1080))

    def draw_wallpaper(self):
        self.win.blit(self.active_wallpaper, (0,0))   #La introduzco en el origen de coordenadas.

    def set_wallpapers_scene(self, scene:str):
        self.load_wallpaper_paths(scene)
        self.set_wallpaper("default")
