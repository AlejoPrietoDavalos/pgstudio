__all__ = ["Clock"]

import pygame as pg

from .typings import T_fps


class Clock:
    """ FIXME: Hacer Singleton."""
    FPS_ALLOWED = frozenset({30, 60})

    def __init__(self, fps: T_fps = 60):
        self.assert_fps(fps)
        self._fps = fps
        self.__clock = pg.time.Clock()

    @property
    def clock(self) -> pg.time.Clock:
        return self.__clock
    
    @property
    def fps(self) -> T_fps:
        return self._fps

    @fps.setter
    def fps(self, new_fps: T_fps) -> None:
        self.assert_fps(new_fps)
        self._fps = new_fps
    
    def tick(self) -> int:
        """ TODO: Esto retorna el número de ns que tardó en ejecutar?"""
        return self.clock.tick(self.fps)
    
    def assert_fps(self, fps: T_fps) -> None:
        assert fps in self.FPS_ALLOWED, f"fps inválido: {fps}"