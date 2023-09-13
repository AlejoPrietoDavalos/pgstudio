import pygame as pg

from functools import cached_property

class ClockPGA:
    def __init__(self, fps: int = 60):
        self.fps = fps
        self.__pg_clock = pg.time.Clock()
    
    # TODO: Setter para fps, que revise que esté dentro de los permitidos.
    
    @property
    def pg_clock(self) -> pg.time.Clock:
        return self.__pg_clock

    @cached_property
    def FPS_ALLOWED(self) -> tuple:
        return (30, 60)
    
    def tick(self) -> int:
        return self.pg_clock.tick(self.fps)     # Esto retorna el número de ns que tardó en ejecutar?

    def change_fps(self, new_fps: int) -> None:
        assert new_fps in self.FPS_ALLOWED, f"FPS inválido. Permitidos: {self.FPS_ALLOWED}"
        self.fps = new_fps