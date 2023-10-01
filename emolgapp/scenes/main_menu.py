from pgstudio.scene import SceneBase
from pgstudio.ui.abc import BoxDrawable, BoxPrinter

import pygame as pg


class MainMenu(SceneBase):
    def __init__(self):
        super().__init__("main_menu")
        #self.btn = BoxDrawable([0,100,300,200], (50,50,50))
        #self.printer = BoxPrinter([0,0,100,100])
    
    def __enter__(self):
        super().__enter__()
        #self.btns
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def fill(self):
        super().fill()
    
    def events(self):
        super().events()
    
    def main(self) -> None:
        #self.btn.move([2,0,-1,1])
        #self.btn.draw()

        #self.printer.on_click()
        pass
