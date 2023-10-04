from pgstudio.scene import SceneBase

#from pgstudio.ui.widgets import 

import pygame as pg


class MainMenu(SceneBase):
    def __init__(self):
        super().__init__("main_menu")
    
    def __enter__(self):
        super().__enter__()
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def fill(self):
        super().fill()
    
    def events(self):
        super().events()
    
    def main(self) -> None:
        pass
