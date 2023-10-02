from abc import ABC, abstractmethod

from pgstudio.display import Window
from pgstudio.config import GameConfig

#from enum import Enum
#class StateApp(Enum):
#    IS_RUNNING
#    PLAYING


class GameApp(ABC):
    """ Objeto principal del juego.

    - FIXME: Esta clase no me convence, modificar. No hace nada relevante,
    hay que ver como implementar el mecanismo de inicio de juego.
    """
    def __init__(self, cfg: GameConfig):
        self.cfg = cfg
        self._is_running = True
        self.window = Window(cfg)

    @property
    def is_running(self) -> bool:
        return self._is_running
    
    @abstractmethod
    def run_app(self) -> None:
        """ TODO: Poner docstring."""
        ...
