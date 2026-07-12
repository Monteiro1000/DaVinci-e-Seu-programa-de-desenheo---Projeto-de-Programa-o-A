from View.opcoes import *
from View.tela import *
from View.cores import *
from Model.figura import *
from Model.linha import *
from Model.elipse import *
from Model.rabisco import *
from Model.retangulo import *
from Model.circulo import *
from Model.quadrado import *
from View.desenha import *

class Mouse:
    def __init__(self, canvas, desenhador, tipo_figura_var):
        self.canvas = canvas
        self.desenhador = desenhador
        self.tipo_figura_var = tipo_figura_var
        self.figura = Linha(cor_figura_var_contorno.get())

        canvas.bind("<ButtonPress-1>", self.clique_no_mouse)
        canvas.bind("<B1-Motion>", self.mover_mouse)
        canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

    def criar_figura(self):

     opcao = self.tipo_figura_var.get()
     cor_contorno = cor_figura_var_contorno.get()
     cor_preenchimento = cor_figura_var_preenchimento.get()

     if opcao == "Linha":
        return Linha(cor_contorno)

     elif opcao == "Elipse":
        return Elipse(cor_contorno, cor_preenchimento)
    
     elif opcao == "Círculo":
        return Circulo(cor_contorno, cor_preenchimento)

     elif opcao == "Retângulo":
        return Retangulo(cor_contorno, cor_preenchimento)

     elif opcao == "Rabisco":
        return Rabisco(cor_contorno)
     
     elif opcao == "Quadrado":
        return Quadrado(cor_contorno, cor_preenchimento)
     

     return Linha(cor_contorno)


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

     def limpar_tela():
        figuras.clear() #esvazia a lista de figuras
        canvas.delete("all") #limpa o canvas

mouse_controller = Mouse(canvas, desenhador, tipo_figura_var)