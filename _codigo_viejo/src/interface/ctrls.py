import pygame as pg

class Ctrls():
    def __init__(self):
        self.mouse = {
            "x": 0,
            "y": 0
        }
        keys = {
            """
            aca hiria, clave la tecla que digo, valor el equivalente en pygame de esa tecla.
            listaria todas las teclas disponibles, para corroborar si fueron pulsadas o no
            en caso de que lo sean, llamo a la acción que desencadena esa tecla en un objeto dado.
            """
        }

    def update_controls(self):
        self.update_mouse_pos()

    def update_mouse_pos(self):
        self.mouse["x"], self.mouse["y"] = pg.mouse.get_pos()

    def ACTUALIZARCONTROLESVERCOMOIMPLEMENTAR(self):
        pass

