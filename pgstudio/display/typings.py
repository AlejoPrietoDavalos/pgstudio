from __future__ import annotations
__all__ = ["Win", "WinRes", "T_fps"]

import pygame as pg

from typing import NewType

Win = NewType("win", pg.Surface)
WinRes = NewType("win_resolution", tuple[int, int])
T_fps = NewType("fps", int)