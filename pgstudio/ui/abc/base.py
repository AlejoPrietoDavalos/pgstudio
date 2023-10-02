from __future__ import annotations
__all__ = ["Drawable", "Clickable"]

from pgstudio.display import Window, T_Win

from abc import ABC, abstractmethod, abstractproperty

from typing import Callable


def if_mouse_up(fn: Callable) -> Callable:
    def wrapper(self: Clickable, *args, **kwargs):
        if self.is_mouse_up:
            return fn(self, *args, **kwargs)
    return wrapper


class Drawable(Window, ABC):
    """ Todo objeto que pueda ser pintado en una `Scene`."""
    @abstractmethod
    def draw(self) -> None:
        """ Especifica la forma en que se usa `self.win` para dibujar."""
        ...
    
    @property
    def win(self) -> T_Win:
        return Window.win
#TODO: class Drawables: collections en widget.


class Clickable(Drawable, ABC):
    @abstractmethod
    def on_click(self) -> None:
        """ Acción a ejecutar cuando se hace click."""
        ...
    
    @abstractproperty
    def is_mouse_up(self) -> bool:
        """ True si el mouse se encuentra encima del objeto."""
        ...

