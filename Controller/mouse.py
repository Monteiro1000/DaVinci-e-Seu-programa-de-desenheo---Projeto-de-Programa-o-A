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

      def selecionar_figura(self, event):
            # Procura a figura clicada no canvas e marca o índice da figura selecionada.
            indice = self.encontrar_figura(event)
            self.figura_selecionada = indice
            if indice is None:
                  self.arrastando = False
                  self.desenhador.desenhar_figura()
                  return

            self.arrastando = True
            self.ultimo_x = event.x
            self.ultimo_y = event.y
            self.desenhador.desenhar_figura()

      def encontrar_figura(self, event):
            for indice in range(len(figuras) - 1, -1, -1):
                  if self.ponto_em_figura(figuras[indice], event.x, event.y):
                        return indice

            return None

      def ponto_em_figura(self, figura, x, y):
            nome = figura[0]
            if nome == "Linha":
                  x1, y1, x2, y2 = figura[1]
                  return self.distancia_ponto_segmento(x, y, x1, y1, x2, y2) <= 5

            if nome == "Rabisco":
                  for indice in range(len(figura[1]) - 1):
                        x1, y1 = figura[1][indice]
                        x2, y2 = figura[1][indice + 1]
                        if self.distancia_ponto_segmento(x, y, x1, y1, x2, y2) <= 5:
                              return True
                  return False

            if nome == "Círculo":
                  centro_x, centro_y, raio = figura[1]
                  return (x - centro_x) ** 2 + (y - centro_y) ** 2 <= raio ** 2

            coordenadas = figura[1]
            if nome == "Elipse":
                  x1, y1, x2, y2 = coordenadas
                  centro_x = (x1 + x2) / 2
                  centro_y = (y1 + y2) / 2
                  raio_x = abs(x2 - x1) / 2
                  raio_y = abs(y2 - y1) / 2
                  if raio_x == 0 or raio_y == 0:
                        return False
                  return ((x - centro_x) ** 2 / raio_x ** 2) + ((y - centro_y) ** 2 / raio_y ** 2) <= 1

            if nome in {"Retângulo", "Quadrado"}:
                  x1, y1, x2, y2 = coordenadas
                  return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

            return False

      def distancia_ponto_segmento(self, x, y, x1, y1, x2, y2):
            if x1 == x2 and y1 == y2:
                  return ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5

            segmento = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if segmento == 0:
                  return float("inf")

            t = max(0, min(1, ((x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)) / segmento ** 2))
            proj_x = x1 + t * (x2 - x1)
            proj_y = y1 + t * (y2 - y1)
            return ((x - proj_x) ** 2 + (y - proj_y) ** 2) ** 0.5

      def mover_figura_selecionada(self, delta_x, delta_y):
            # Atualiza a posição da figura marcada aplicando o deslocamento do arraste do mouse.
            if self.figura_selecionada is None:
                  return

            figura = figuras[self.figura_selecionada]
            nome = figura[0]
            if nome == "Rabisco":
                  pontos = [(ponto[0] + delta_x, ponto[1] + delta_y) for ponto in figura[1]]
                  figuras[self.figura_selecionada] = (nome, pontos, figura[2])
            elif nome == "Círculo":
                  centro_x, centro_y, raio = figura[1]
                  figuras[self.figura_selecionada] = (nome, (centro_x + delta_x, centro_y + delta_y, raio), figura[2], figura[3])
            else:
                  x1, y1, x2, y2 = figura[1]
                  figuras[self.figura_selecionada] = (nome, (x1 + delta_x, y1 + delta_y, x2 + delta_x, y2 + delta_y), *figura[2:])

            self.desenhador.desenhar_figura()

      def apagar_selecionada(self, event=None):
            if self.figura_selecionada is None:
                  return
            figuras.pop(self.figura_selecionada)
            self.figura_selecionada = None
            self.desenhador.desenhar_figura()

      def mover_para_frente(self, event=None):
            if self.figura_selecionada is None:
                  return
            indice = self.figura_selecionada
            if indice < len(figuras) - 1:
                  figuras.insert(indice + 1, figuras.pop(indice))
                  self.figura_selecionada = indice + 1
                  self.desenhador.desenhar_figura()

      def mover_para_tras(self, event=None):
            if self.figura_selecionada is None:
                  return
            indice = self.figura_selecionada
            if indice > 0:
                  figuras.insert(indice - 1, figuras.pop(indice))
                  self.figura_selecionada = indice - 1
                  self.desenhador.desenhar_figura()

      def mover_para_topo(self, event=None):
            if self.figura_selecionada is None:
                  return
            indice = self.figura_selecionada
            figuras.append(figuras.pop(indice))
            self.figura_selecionada = None
            self.desenhador.desenhar_figura()

      def mover_para_fundo(self, event=None):
            if self.figura_selecionada is None:
                  return
            indice = self.figura_selecionada
            figuras.insert(0, figuras.pop(indice))
            self.figura_selecionada = 0
            self.desenhador.desenhar_figura()

      def copiar_selecionada(self, event=None):
            # Guarda uma cópia da figura selecionada para uso posterior com CTRL-C/CTRL-V.
            if self.figura_selecionada is None:
                  return
            self.buffer = copy.deepcopy(figuras[self.figura_selecionada])
            self.desenhador.desenhar_figura()

      def colar_selecionada(self, event=None):
            # Insere a figura copiada no canvas deslocando-a levemente para evitar sobreposição.
            if self.buffer is None:
                  return

            figura_copiada = copy.deepcopy(self.buffer)
            if figura_copiada[0] == "Rabisco":
                  pontos = [(ponto[0] + 10, ponto[1] + 10) for ponto in figura_copiada[1]]
                  figura_copiada = (figura_copiada[0], pontos, figura_copiada[2])
            else:
                  x1, y1, x2, y2 = figura_copiada[1]
                  figura_copiada = (figura_copiada[0], (x1 + 10, y1 + 10, x2 + 10, y2 + 10), *figura_copiada[2:])

            figuras.append(figura_copiada)
            self.figura_selecionada = len(figuras) - 1
            self.desenhador.desenhar_figura()

      def limpar_tela(self):
         figuras.clear() #esvazia a lista de figuras
         self.canvas.delete("all") #limpa o canvas

mouse_controller = Mouse(canvas, desenhador, tipo_figura_var)