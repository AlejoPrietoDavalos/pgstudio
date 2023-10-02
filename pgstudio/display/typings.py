from __future__ import annotations
__all__ = ["T_Win", "WinRes"]

import pygame as pg

from typing import NewType

T_Win = NewType("win", pg.Surface)
WinRes = NewType("resolution", tuple[int, int])