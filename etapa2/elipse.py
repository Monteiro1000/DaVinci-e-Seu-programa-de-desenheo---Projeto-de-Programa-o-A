from figura import *
from tela import *
from opcoes import *

class Elipse(Figura):

    def __init__(self):
        super().__init__("Elipse", None, None)

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

        self.cor_contorno = dicionario_cores[cor_figura_var_contorno.get()] #associa a cor escolhida ao dicionario de cores (contorno)
        self.cor_preenchimento = dicionario_cores[cor_figura_var_preenchimento.get()]#associa a cor escolhida ao dicionario de cores (preenchimento)

    # Quando o mouse é pressionado
    def inicia_figura(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

        self.fim_x = event.x
        self.fim_y = event.y

    # Quando o mouse é movido
    def atualiza_figura(self, event):

        self.fim_x = event.x
        self.fim_y = event.y

        
        self.desenhar_figura()

        if not self.incompleta():
            canvas.create_oval(
                self.ini_x,
                self.ini_y,
                self.fim_x,
                self.fim_y,
                dash=(4, 2),
                outline=self.cor_contorno
            )
        

    # Quando o mouse é solto
    def incluir_figura(self, event):

        if self.incompleta():

            self.desenhar_figura
            return

        self.coordenadas = (
            self.ini_x,
            self.ini_y,
            self.fim_x,
            self.fim_y
        )

        figuras.append(
            (self.nome, self.coordenadas, self.cor_contorno, self.cor_preenchimento)
        )

        self.desenhar_figura()

    def desenhar_figura(self):
         canvas.delete("all") # Limpa os rastros antigos

         for figura in figuras:
            if figura[0] == "Linha":
                canvas.create_line(figura[1][0], figura[1][1], figura[1][2], figura[1][3], fill=figura[2])

            elif figura[0] == "Elipse":
                canvas.create_oval(figura[1][0], figura[1][1], figura[1][2], figura[1][3], 
                                   outline=figura[2], fill=figura[3])
            
            elif figura[0] == "Círculo":
                nome, coordenadas, cor_contorno, cor_preenchimento = figura #separa os dados de circulo
                canvas.create_oval(coordenadas[0]-coordenadas[2], coordenadas[1]-coordenadas[2],
                                   coordenadas[0]+coordenadas[2], coordenadas[1]+coordenadas[2],
                                    outline=cor_contorno, fill=cor_preenchimento )

            elif figura[0] == "Rabisco":
                nome, values, cor = figura # separa a variavel em parametros diferentes
                canvas.create_line(values, fill=cor)

            elif figura[0] == "Retângulo":
                canvas.create_rectangle(figura[1][0], figura[1][1], figura[1][2], figura[1][3],
                                         outline=figura[2], fill=figura[3])
        


    def incompleta(self):
        return (
            self.ini_x == self.fim_x or
            self.ini_y == self.fim_y
        )