from Model.figura import *

class Quadrado(Figura):
    def __init__(self, cor_contorno, cor_preenchimento):
        super().__init__("Quadrado", None, None)
        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None

        self.cor_contorno = cor_contorno
        self.cor_preenchimento = cor_preenchimento
    def inicia_figura(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def atualiza_figura(self, event):
        self.fim_x = event.x
        distancia_x = self.fim_x-self.ini_x
        self.fim_y = self.ini_y+distancia_x
        
    def incluir_figura(self, event): 

        if self.incompleta():

            return  # Não desenha se o quadrado for incompleto
    
        self.coordenadas = (self.ini_x, self.ini_y, self.fim_x, self.fim_y)

        #Guardamos uma tupla contendo: (tipo_da_figura, coordenadas, cor)
        figuras.append(("Quadrado", self.coordenadas, self.cor_contorno, self.cor_preenchimento))




    def incompleta(self):
        return self.ini_x == self.fim_x or self.ini_y == self.fim_y