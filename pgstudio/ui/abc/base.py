from __future__ import annotations
__all__ = ["WinAccess", "VisualElem"]

from pgstudio.display import Window, T_Win, WinRes

from abc import ABC, abstractmethod


#----------Basics----------

class WinAccess(ABC):
    """ Todo objeto con acceso a `Window.win`."""
    @property
    def win(self) -> T_Win:
        """ `pg.Surface` que contiene la ventana."""
        return Window.win
    
    @property
    def res(self) -> WinRes:
        """ Resolución de pantalla."""
        return Window.res


class Drawable(WinAccess, ABC):
    """ Todo objeto que pueda ser pintado en una `Scene`."""
    @abstractmethod
    def draw(self) -> None:
        """ Dibuja al objeto usando `self.win`."""
        ...


class Updatable(ABC):
    """ Todo objeto que pueda cambiar sus atributos en tiempo de ejecución."""
    @abstractmethod
    def update(self) -> None:
        """ Actualizar los atributos del objeto en cada frame."""
        ...


class Clickable(ABC):
    ...

#----------Combinations----------






class DrawableUpdatable(Drawable, Updatable, ABC):
    @abstractmethod
    def draw(self) -> None: ...
    @abstractmethod
    def update(self) -> None: ...


class VisualElem(DrawableUpdatable, ABC):
    """
    Todo objeto que se muestre en escena, debe acceder a `Window.win`
    para dibujarse, y un mecanismo implementado para el `update()`.
    """
    @abstractmethod
    def draw(self) -> None: ...
    @abstractmethod
    def update(self) -> None: ...



#TODO: class Drawables: collections en widget.



'''
class Clickable(Drawable, ABC):
    @abstractmethod
    def on_click(self) -> None:
        """ Acción a ejecutar cuando se hace click."""
        ...
    
    @abstractproperty
    def is_mouse_up(self) -> bool:
        """ True si el mouse se encuentra encima del objeto."""
        ...

        
def if_mouse_up(fn: Callable) -> Callable:
    def wrapper(self: Clickable, *args, **kwargs):
        if self.is_mouse_up:
            return fn(self, *args, **kwargs)
    return wrapper
'''
