import pgstudio as pgs
from pgstudio.config import GameConfig

from emolgapp.scenes.main_menu import MainMenu

class EmolgApp(pgs.GameApp):
    def __init__(self, cfg: GameConfig):
        super().__init__(cfg=cfg)
    
    def run_app(self) -> None:
        scene = MainMenu()
        scene.main_loop()