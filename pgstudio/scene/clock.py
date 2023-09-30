import pygame as pg


class Clock:
    FPS_ALLOWED = frozenset({30, 60})

    def __init__(self, fps: int = 60):
        self.assert_fps(fps)
        self.fps = fps
        self.__pg_clock = pg.time.Clock()
    
    @property
    def pg_clock(self) -> pg.time.Clock:
        return self.__pg_clock
    
    def tick(self) -> int:
        return self.pg_clock.tick(self.fps)     # Esto retorna el número de ns que tardó en ejecutar?

    def set_fps(self, new_fps: int) -> None:
        self.assert_fps(new_fps)
        self.fps = new_fps
    
    def assert_fps(self, fps: int) -> None:
        assert fps in self.FPS_ALLOWED, f"fps inválido: {fps}"