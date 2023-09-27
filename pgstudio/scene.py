from __future__ import annotations
from abc import ABC, abstractmethod

import pygame as pg
from pygame.event import Event

from functools import cached_property

from pgstudio.clock import ClockPGA
from pgstudio.window import Window
from pgstudio.ui.widget import BtnsScene


from typing import NewType, Dict, List


SceneName = NewType("scene_name", str)

class Scene(Window, ABC):
    """
    Clase abstracta para el manejo de `Scenes`.

    Implementar:
    ------------
    - `__enter__`: Se ejecuta al entrar en la escena.
    - `__exit__`: Se ejecuta al salir de la escena.
    - `fill`: Se ejecuta en cada iteración para rellenar el fondo.
    - FIXME `events`: Revisa los eventos.
    - `main`: Loop principal de la escena.
    """
    clock = pg.time.Clock()     # ClockPGA(60)
    fps = 60
    """ Abstract class para `Scene` de pygame."""
    def __init__(self, name: SceneName):
        self.__name = name
        self._is_running = False
        self.btns = BtnsScene()

    @property
    def name(self) -> SceneName:
        return self.__name

    @property
    def is_running(self) -> bool:
        return self._is_running

    @abstractmethod
    def __enter__(self) -> None:
        """ Se ejecuta al `entrar` en la escena. """
        self.start()
    
    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """ Se ejecuta al `salir` de la escena."""
        ...
    
    @abstractmethod
    def fill(self) -> None:
        """ Como rellenar el fondo. Por default se pinta de negro."""
        self.win.fill("black")
    
    @abstractmethod
    def events(self) -> None:
        """
        - TODO: Podría ser que cada objeto que interactúe con un evento
        tenga una forma rápida de acceder a los eventos que se dieron, quizás
        con un diccionario puede ser bueno hacerlo.
        - FIXME: Quizas se podría agregar que el evento sea pasado por default a la función main.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.stop()
    
    @abstractmethod
    def main(self) -> None:
        """ Se ejecuta en cada iteración."""
        ...
    
    def start(self) -> None:
        self._is_running = True

    def stop(self) -> None:
        self._is_running = False

    def main_loop(self) -> None:
        """ Loop principal de la escena.
        - TODO: Ver de retornar un objeto que guarde el código de respuesta."""
        with self:
            while self.is_running:
                self.main()
                self.events()
                self.clock.tick(self.fps)   # TODO: Eventualmente estará envuelta en otra clase.
                pg.display.update()
                self.fill()





















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