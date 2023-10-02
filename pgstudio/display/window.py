from __future__ import annotations
__all__ = ["Window"]

import pygame as pg

from .clock import Clock

from .typings import T_Win, WinRes

class Window:
    """ FIXME: Encapsular."""
    _instance = None
    win: T_Win
    app_name: str
    res: WinRes
    clock: Clock = None

    def __new__(cls, app_name: str, res: WinRes, fps: int):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Window, cls).__new__(cls)
            cls.win = pg.display.set_mode(res)
            
            cls.app_name = app_name
            pg.display.set_caption(app_name)

            cls.res = res
            cls.clock = Clock(fps=fps)
        return cls._instance

    @classmethod
    def refresh(cls) -> None:
        cls.clock.tick()
        pg.display.update()
