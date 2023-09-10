from typing import Callable
#from .buttons import Buttons

class ButtonWrappers:
    def refresh_mouse_up(func:Callable):
        """ Revisa si el mouse se encuentra encima del botón,
            y cambia mouse_up en consecuencia."""
        def wrapper(btn, *args, **kwargs):
            if (btn.pos_btn["x"] <= btn.ctrls.mouse["x"] <= btn.pos_btn["x"]+btn.pos_btn["w"] and
                btn.pos_btn["y"] <= btn.ctrls.mouse["y"] <= btn.pos_btn["y"]+btn.pos_btn["h"]):
                btn.mouse_up = True
            else:
                btn.mouse_up = False
            func(btn, *args, **kwargs)
        return wrapper

    def check_mouse_up(func:Callable):
        """ Ejecuta la función si y solo si, mouse_up=True."""
        def wrapper(btn, *args, **kwargs):
            if btn.mouse_up:
                func(btn, *args, **kwargs)
        return wrapper

    def check_is_active(func:Callable):
        """ Ejecuta la función si y solo si, is_active=True."""
        def wrapper(btn, *args, **kwargs):
            if btn.is_active:
                func(btn, *args, **kwargs)
        return wrapper

