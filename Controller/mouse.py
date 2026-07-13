from View.opcoes import *
from View.tela import *
from View.cores import *
from View.opcoes import *
from Model.figura import *
from Model.linha import *
from Model.elipse import *
from Model.rabisco import *
from Model.retangulo import *
from Model.circulo import *
from Model.quadrado import *
from View.desenha import *
from Controller.ferramenta_linha import * 
from Controller.ferramenta_retangulo import *
from Controller.ferramenta_rabisco import *
from Controller.ferramenta_circulo import *
from Controller.ferramenta_elipse import *
from Controller.ferramenta_quadrado import *


class Mouse:
      def __init__(self, canvas, desenhador, tipo_figura_var):
            
            #designacao de variaveis do canvas, desenhador e do tipo de figura
            self.canvas = canvas
            self.desenhador = desenhador
            self.tipo_figura = tipo_figura_var


            #criacao das instancias de cada ferramenta
            self.ferramentas = {
                  "Linha": Linha_Ferramenta(self.canvas, self.desenhador),
                  "Retângulo": Retangulo_Ferramenta(self.canvas, self.desenhador),
                  "Rabisco": Rabisco_Ferramenta(self.canvas, self.desenhador),
                  "Círculo": Circulo_Ferramenta(self.canvas, self.desenhador),
                  "Elipse": Elipse_Ferramenta(self.canvas, self.desenhador),
                  "Quadrado": Quadrado_Ferramenta(self.canvas, self.desenhador),
            }
            
            #ferramenta inicial
            self.ferramenta_desenho = self.ferramentas["Linha"]

            #serve para reagir quando muda a opcao da figura 
            self.tipo_figura.trace("w", self.muda_ferramenta)


            #Eventos do mouse para os desenhos no canvas
            canvas.bind("<ButtonPress-1>", self.clique_no_mouse)
            canvas.bind("<B1-Motion>", self.mover_mouse)
            canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

      # Ao mudar o option menu que escolhe a ferramenta de desenho essa funcao muda a ferramenta escolhida
      def muda_ferramenta(self, *args):
            nome_ferramenta = self.tipo_figura.get()
            self.ferramenta_desenho = self.ferramentas.get(nome_ferramenta, self.ferramentas["Linha"])
      



      def clique_no_mouse(self, event):

         self.ferramenta_desenho.mouse_pressionado(event)


      def mover_mouse(self, event):
         self.ferramenta_desenho.mouse_arrastado(event)


      def soltar_mouse(self, event):
         self.ferramenta_desenho.mouse_solto(event)

      def limpar_tela():
         figuras.clear() #esvazia a lista de figuras
         canvas.delete("all") #limpa o canvas

mouse_controller = Mouse(canvas, desenhador, tipo_figura_var)