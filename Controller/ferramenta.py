from abc import ABC, abstractmethod
from tkinter import *
from View.tela  import *
from View.desenha import *
from dataclasses import dataclass

@dataclass
class Ferramenta(ABC):
    desenho: Desenha
    tela : Tela

    def __post_init__(self):
        self.canvas = app_tela.canvas

    @abstractmethod
    def mouse_pressionado(self, event):
        pass

    @abstractmethod
    def mouse_arrastado(self, event):
        pass

    @abstractmethod
    def mouse_solto(self, event):
        pass