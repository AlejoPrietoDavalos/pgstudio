from __future__ import annotations
__all__ = ["Window"]

from .clock import Clock

import pygame as pg

from .typings import T_Win, T_WinRes


class Window:
    """ FIXME: Encapsular."""
    _instance = None
    win: T_Win
    app_name: str
    resolution: T_WinRes
    clock: Clock = None

    def __new__(cls, app_name: str, resolution: T_WinRes, fps: int):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Window, cls).__new__(cls)
            cls.win = pg.display.set_mode(resolution)
            
            cls.app_name = app_name
            pg.display.set_caption(app_name)

            cls.resolution = resolution
            cls.clock = Clock(fps=fps)
        return cls._instance

    @classmethod
    def refresh(cls) -> None:
        cls.clock.tick()
        pg.display.update()
