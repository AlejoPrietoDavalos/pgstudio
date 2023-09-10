import pygame as pg
import sys

def _loops_scenes_imports() -> dict:
    """ Se hacen los imports de todas las escenas dentro del
        juego y se vuelve un diccionario con el loop de cada escena."""
    from .main_menu import loop_main_menu
    return {
        "main_menu": loop_main_menu,
    }

class Router():
    def __init__(self):
        _FIRST_SCENE = "main_menu"
        self._TO_LOOP_SCENE = _loops_scenes_imports()
        self.SCENES = tuple(self._TO_LOOP_SCENE.keys())
        
        
        self.run = True
        self._state_scenes = {scene: False for scene in self.SCENES}                      # Será True la escena activa.
        self._state_scenes[_FIRST_SCENE] = True
    
    def go_to_scene(self, scene:str, *args, **kwargs):
        self._TO_LOOP_SCENE[scene](scene, *args, **kwargs)

    def is_active_scene(self, scene:str):
        return self._state_scenes[scene]

    def change_scene(self, new_scene:str):
        self.close_all_scenes()
        self._state_scenes[new_scene] = True      # Y luego vuelvo True la que me interesa.

    def close_all_scenes(self):
        for scene in self.SCENES:
            if self._state_scenes[scene]:
                self._state_scenes[scene] = False      # Seteo todas las escenas a False.

    def close_the_game(self):
        self.close_all_scenes()
        self.run = False
        pg.quit()
        sys.exit()