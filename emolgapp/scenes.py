from pygameapp.scene import Scene
#import pygameapp.ui.btn import 

import pygame as pg

class ScenesNames:
    main_menu: str = "main_menu"

class MainMenu(Scene):
    def __init__(self):
        super().__init__(ScenesNames.main_menu)
        self.coords = [0,100,300,200]
    
    def __enter__(self):
        super().__enter__()
        # Poner todos los botones.
    
    def __exit__(self, exc_type, exc_value, traceback):
        #return super().__exit__(exc_type, exc_value, traceback)
        pass
    
    def main(self) -> None:
        #[x,y,w,h]
        self.coords[0] += 1
        pg.draw.rect(self.win, (50,50,50), self.coords)

