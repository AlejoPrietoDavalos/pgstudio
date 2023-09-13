from __future__ import annotations
from abc import ABC, abstractmethod

import pygame as pg
from pygame import QUIT

from functools import cached_property

from typing import Dict, Callable, Any, NewType

from pygameapp.clock import ClockPGA

SceneName = NewType("scene_name", str)





class Scene(ABC):
    """ Abstract class para `Scene` de pygame."""
    def __init__(self, name: str):
        self.__name = name
        self._is_running = False

    @property
    def name(self) -> SceneName:
        return self.__name

    @property
    def is_running(self) -> bool:
        return self._is_running

    @abstractmethod
    def __enter__(self):
        """ Se ejecuta al entrar en la escena."""
        pass
    
    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """ Se ejecuta al salir de la escena."""
        pass
    
    @abstractmethod
    def main(self):
        """ Se ejecuta en cada iteración."""
        pass
    
    def start(self) -> None:
        self._is_running = True

    def stop(self) -> None:
        """ Ejecuta hasta la próxima iteración."""
        self._is_running = False
    
    @staticmethod
    def load(name: str) -> Scene:
        # TODO: Ver como usar el `partial` de functools, para no repetir atributos.
        return Scene(name=name)

    def main_loop(self):
        """ Loop principal de la escena."""
        with self:
            while self.is_running:
                self.main()


class DictScenes(Dict[SceneName, Scene]):
    """ `current_name` (str): """
    def __init__(self, first_scene: str, fps: int = 60):
        super().__init__()
        self._current_name = first_scene
        self.clock = ClockPGA(fps=fps)
    
    @cached_property
    def SCENES_PERMITIDAS(self) -> tuple[str]:
        return ("test_scene", "sarasa")

    @property
    def current_name(self) -> SceneName:
        return self._current_name

    @property
    def current(self) -> Scene:
        return super().__getitem__(self._current_name)
    
    def __setitem__(self, scene_name: SceneName, scene: Scene) -> None:
        assert not self.__contains__(scene)
        super().__setitem__(scene_name, scene)
    
    def __contains__(self, __key: SceneName | Scene) -> bool:
        if isinstance(__key, str):
            return __key in self
        elif isinstance(__key, Scene):
            return __key.name in self
        raise Exception("Key inválida.")

    def add_scene(self, scene: Scene) -> None:
        """ TODO: Podría ser paralelo."""
        assert isinstance(scene, Scene)
        self.assert_scene(scene.name)
        super().__setitem__(scene.name, scene)
    
    def change_scene(self, new_scene_name: SceneName) -> None:
        self.assert_scene(new_scene_name)
        self._current_name = new_scene_name
    
    def assert_scene(self, scene_name) -> None:
        """ TODO: Eventualmente podría ser una lista, y que sea varabiale."""
        assert scene_name in self.SCENES_PERMITIDAS, "Scene no está dentro de las permitidas."


class Scenes(DictScenes):
    pass


class TestScene(Scene):
    def __init__(self):
        pass


class SpecificScenes(DictScenes):
    def __init__(self, fps):
        super().__init__(fps)
    
    def main(self):
        while self.current.run:
            self.current.main()
            self.clock.tick()

#    """
#    - TODO: Si no deleteo la Scena como key-value, seestá guardando la
#    información de la escena. Y se podría volver,sería como una especie de 'cache'.
#    - TODO: También recordar como definir el __getitem__ y __setitem__, que cree las escenas.
#    """





#def scene_wrap(fn_main_loop: Callable) -> Callable:
#    """ Wrapper para la función main de la escena. Ver como adaptar luego."""
#    def wrapper(self, *args, **kwargs) -> Any:
#        result = fn_main_loop(self, *args, **kwargs)
#        self.clock.tick()
#        return result
#    return wrapper