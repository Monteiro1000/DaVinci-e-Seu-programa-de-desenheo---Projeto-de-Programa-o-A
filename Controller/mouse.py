from View.opcoes import *
from View.tela import *
from Model.figura import *
from Model.linha import *
from Model.elipse import *
from Model.rabisco import *
from Model.retangulo import *
from Model.circulo import *

class Mouse:
    def __init__(self, canvas, desenhador, tipo_figura_var):
        self.canvas = canvas
        self.desenhador = desenhador
        self.tipo_figura_var = tipo_figura_var
        self.figura = Linha()

        canvas.bind("<ButtonPress-1>", self.clique_no_mouse)
        canvas.bind("<B1-Motion>", self.mover_mouse)
        canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

    def criar_figura(self):

     opcao = self.tipo_figura_var.get()

     if opcao == "Linha":
        return Linha()

     elif opcao == "Elipse":
        return Elipse()
    
     elif opcao == "Círculo":
        return Circulo()

     elif opcao == "Retângulo":
        return Retangulo()

     elif opcao == "Rabisco":
        return Rabisco()

     return Linha()


    def clique_no_mouse(self, event):

      self.figura = self.criar_figura()
      self.figura.inicia_figura(event)


    def mover_mouse(self, event):
      self.figura.atualiza_figura(event)
      self.desenhador.desenhar_figura()
      if self.figura.incompleta():
        return
      self.desenhador.desenha_temporaria(self.figura)


    def soltar_mouse(self, event):
     self.figura.incluir_figura(event)
     if self.figura.incompleta():
        return
     self.desenhador.desenhar_figura()


