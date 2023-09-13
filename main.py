import pygame as pg

from pygameapp.scene import Scene, SpecificScenes


class PyGameApp:
    def __init__(self, scenes: SpecificScenes, app_name: str):
        pg.init()
        pg.display.set_caption(app_name)
        self.screen = pg.display.set_mode((960, 540))
        
        self.scenes = scenes

    def run_app(self) -> None:
        """ Ejecuta el método main de `scenes`."""
        self.scenes.main()

_scenes = SpecificScenes(fps=60)
_scenes.add_scene(Scene("primera"))

pgapp = PyGameApp(
    scenes = _scenes,
    app_name = "EmolgApp"
)

pgapp.run_app()
