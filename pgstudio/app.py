from abc import ABC, abstractmethod

from pgstudio.display import Window, T_WinRes




#from enum import Enum
#class StateApp(Enum):
#    IS_RUNNING
#    PLAYING


class GameApp(ABC):
    """ Objeto principal del juego.

    - FIXME: Esta clase no me convence, modificar. No hace nada relevante,
    hay que ver como implementar el mecanismo de inicio de juego.
    """
    def __init__(self, app_name: str, resolution: T_WinRes, fps: int):
        self._is_running = True
        self.window = Window(
            app_name = app_name,
            resolution = resolution,
            fps = fps
        )

    @property
    def is_running(self) -> bool:
        return self._is_running
    
    @abstractmethod
    def run_app(self) -> None:
        """ TODO: Poner docstring."""
        ...
