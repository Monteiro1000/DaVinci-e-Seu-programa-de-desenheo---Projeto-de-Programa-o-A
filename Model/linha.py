from Model.figura import *



class Linha(Figura):

    def __init__(self, cor):
        super().__init__("Linha", None, None)

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

        self.cor = cor

    # Quando o mouse é pressionado
    def inicia_figura(self, event):
        self.ini_x = event.x
        self.ini_y = event.y
        self.fim_x = event.x
        self.fim_y = event.y

    # Quando o mouse é movido com o botão pressionado
    def atualiza_figura(self, event):

        self.fim_x = event.x
        self.fim_y = event.y


    # Quando o mouse é solto
    def incluir_figura(self, event):
        self.coordenadas = (
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y
        )

        if self.incompleta():

            return

        
        figuras.append(
            (self.nome, self.coordenadas, self.cor)
        )


    
        
    def incompleta(self):
        return (
            self.ini_x == self.fim_x and
            self.ini_y == self.fim_y
        )

