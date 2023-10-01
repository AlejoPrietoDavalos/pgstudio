from __future__ import annotations
__all__ = ["T_Win", "T_WinRes"]

import pygame as pg

from typing import NewType

T_Win = NewType("win", pg.Surface)
T_WinRes = NewType("win_res", tuple[int, int])