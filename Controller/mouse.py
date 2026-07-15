import copy
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
            self.figura_selecionada = None
            self.arrastando = False
            self.ultimo_x = 0
            self.ultimo_y = 0
            self.buffer = None

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
            canvas.bind_all("<Delete>", self.apagar_selecionada)
            canvas.bind_all("<Right>", self.mover_para_frente)
            canvas.bind_all("<Left>", self.mover_para_tras)
            canvas.bind_all("<Up>", self.mover_para_topo)
            canvas.bind_all("<Down>", self.mover_para_fundo)
            canvas.bind_all("<Control-c>", self.copiar_selecionada)
            canvas.bind_all("<Control-v>", self.colar_selecionada)

      # Ao mudar o option menu que escolhe a ferramenta de desenho essa funcao muda a ferramenta escolhida
      def muda_ferramenta(self, *args):
            nome_ferramenta = self.tipo_figura.get()
            if nome_ferramenta == "Seleção":
                  self.ferramenta_desenho = None
            else:
                  self.ferramenta_desenho = self.ferramentas.get(nome_ferramenta, self.ferramentas["Linha"])
      


      def clique_no_mouse(self, event):
         self.canvas.focus_set()
         if self.tipo_figura.get() == "Seleção":
               # Seleciona a figura clicada para executar as operações de edição
               self.selecionar_figura(event)
               return

         self.ferramenta_desenho.mouse_pressionado(event)


      def mover_mouse(self, event):
         if self.tipo_figura.get() == "Seleção":
               # Move a figura selecionada enquanto o botão esquerdo do mouse é arrastado
               if self.arrastando and self.figura_selecionada is not None:
                     self.mover_figura_selecionada(event.x - self.ultimo_x, event.y - self.ultimo_y)
                     self.ultimo_x = event.x
                     self.ultimo_y = event.y
               return

         self.ferramenta_desenho.mouse_arrastado(event)


      def soltar_mouse(self, event):
         if self.tipo_figura.get() == "Seleção":
               self.arrastando = False
               self.desenhador.desenhar_figura()
               return

         self.ferramenta_desenho.mouse_solto(event)

      def limpar_tela():
         figuras.clear() #esvazia a lista de figuras
         canvas.delete("all") #limpa o canvas

mouse_controller = Mouse(canvas, desenhador, tipo_figura_var)