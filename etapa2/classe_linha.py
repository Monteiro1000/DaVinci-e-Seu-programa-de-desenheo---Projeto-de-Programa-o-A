from classe_figura import *
from tela_figuras import *


class Linha(Figura):

    def __init__(self):
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

        self.cor = "black"

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

        self.desenhar_figura()

        canvas.create_line(
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y,
            dash=(4, 2),
            fill=self.cor
        )

    # Quando o mouse é solto
    def incluir_figura(self, event):

        if self.incompleta():
            return

        self.coordenadas = (
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y
        )

        figuras.append(
            (self.nome, self.coordenadas, self.cor)
        )

        self.desenhar_figura()

    def desenhar_figura(self):

        canvas.delete("all")

        for figura in figuras:

            if figura[0] == "Linha":

                canvas.create_line(
                    figura[1][0],
                    figura[1][1],
                    figura[1][2],
                    figura[1][3],
                    fill=figura[2]
                )

            elif figura[0] == "Elipse":

                canvas.create_oval(
                    figura[1][0],
                    figura[1][1],
                    figura[1][2],
                    figura[1][3],
                    outline=figura[2]
                )
            
            elif figura[0] == "Rabisco":
                nome, values, cor = figura
                canvas.create_line(values, fill=cor)

    def incompleta(self):
        return (
            self.ini_x == self.fim_x and
            self.ini_y == self.fim_y
        )

