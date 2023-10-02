from __future__ import annotations
__all__ = ["Window"]

import pygame as pg

from pgstudio.config import GameConfig
from .clock import Clock

from .typings import T_Win, WinRes

class Window:
    """ FIXME: Encapsular."""
    _instance = None
    win: T_Win
    app_name: str
    resolution: WinRes
    clock: Clock = None

    def __new__(cls, cfg: GameConfig):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Window, cls).__new__(cls)
            cls.win = pg.display.set_mode(cfg.res)
            
            cls.app_name = cfg.app_name
            pg.display.set_caption(cfg.app_name)

            cls.resolution = cfg.res
            cls.clock = Clock(fps=cfg.fps)
        return cls._instance

    @classmethod
    def refresh(cls) -> None:
        cls.clock.tick()
        pg.display.update()
