""" Este módulo contiene la clase base para widgets. """
from __future__ import annotations
from abc import ABC, abstractmethod

class Widget(ABC):
    """ Clase abstracta para widgets."""

    @abstractmethod
    def is_mouse_up(self):
        pass

    @abstractmethod
    def on_click(self):
        pass



