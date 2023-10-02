import pgstudio as pgs
from pgstudio.config import ConfigApp

from emolgapp.scenes.main_menu import MainMenu

class EmolgApp(pgs.GameApp):
    def __init__(self, cfg_app: ConfigApp):
        super().__init__(cfg_app=cfg_app)
    
    def run_app(self) -> None:
        scene = MainMenu()
        scene.main_loop()