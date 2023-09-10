from src.interface.ui import UI
from .scenes.router import Router

class MainManager():
    def __init__(self):
        self.ui = UI()
        self.ROUTER = Router()

    def main_loop(self):
        while self.ROUTER.run:
            for scene in self.ROUTER.SCENES:
                if self.ROUTER.is_active_scene(scene):
                    # Realizamos todas las acciones que queremos que se hagan antes de cambiar de escena.
                    self.ui.before_changing_scene(scene)
                    
                    # Entro en el loop de la escena que está activa.
                    self.ROUTER.go_to_scene(scene, self.ui, self.ROUTER)
                    
                    # Guardamos los botones al salir de la escena
                    self.ui.btns.save_scene_buttons(scene)
