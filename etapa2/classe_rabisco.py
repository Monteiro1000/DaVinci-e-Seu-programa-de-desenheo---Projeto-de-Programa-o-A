from classe_figura import *
from tela_figuras import *

class Rabisco(Figura):

    def __init__(self):
        super().__init__(nome="Rabisco", coordenadas=None, cor="Black")
        
    def inicia_figura(self, event):
        self.coordenadas= [(event.x, event.y)]

    def atualiza_figura(self, event):
        self.coordenadas.append((event.x, event.y))
        canvas.create_line(self.coordenadas, dash=(4, 2), fill=self.cor)
    
    def incluir_figura(self, event):
        if self.incompleta():
            return # Não desenha se o rabisco for incompleto
        figuras.append((self.nome,self.coordenadas, self.cor))  # Adiciona o rabisco à lista de figuras desenhadas
        self.desenhar_figuras()

    def desenhar_figuras(self):
        canvas.delete("all")
        for figura in figuras:
            if figura[0] == "Rabisco":
                nome, values, cor = figura
                canvas.create_line(values, fill=cor)
            
            
            elif figura[0] == "Linha":

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
            

    def incompleta(self):
        return len(self.coordenadas)  <= 1

