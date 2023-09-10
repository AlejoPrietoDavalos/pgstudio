import pygame as pg
pg.init()
pg.display.set_caption("EmolgApp Online")
import os
os.system("clear")
from src.main_manager import MainManager

if __name__ == "__main__":
    MAIN_MANAGER = MainManager()
    MAIN_MANAGER.main_loop()