from Model.figura import *


class Circulo(Figura):

    def __init__(self, cor_contorno, cor_preenchimento):
        super().__init__("Círculo", None, None)

        self.cor = "black"

        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None

        self.coordenadas = (
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y
        )

        self.cor_contorno = cor_contorno
        self.cor_preenchimento = cor_preenchimento
    # Quando o mouse é pressionado
    def inicia_figura(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    # Quando o mouse é movido
    def atualiza_figura(self, event):

        self.fim_x = event.x
        self.fim_y = event.y
     
        
        self.raio = ( (self.ini_x - self.fim_x)**2 + (self.ini_y - self.fim_y)**2 ) ** 0.5 #calcula o raio do circulo

        

    # Quando o mouse é solto
    def incluir_figura(self, event):

        if self.incompleta():
            return

        self.coordenadas = (
            self.ini_x,
            self.ini_y,
            self.raio
        )

        figuras.append(
            ("Círculo", self.coordenadas, self.cor_contorno, self.cor_preenchimento)
        )



    
         

    def incompleta(self):
          return (
             self.ini_x == self.fim_x or
            self.ini_y == self.fim_y
        )
        