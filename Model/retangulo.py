from Model.figura import *
from View.tela import *
from View.opcoes import *
from View.cores import*

class Retangulo(Figura):
    def __init__(self):
        super().__init__("Retângulo", None, None)
        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None

        self.cor_contorno = cor_figura_var_contorno.get() #associa a cor escolhida ao objeto (contorno)
        self.cor_preenchimento = cor_figura_var_preenchimento.get() #associa a cor escolhida ao objeto (preenchimento)

    def inicia_figura(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    def atualiza_figura(self, event):
        self.fim_x = event.x
        self.fim_y = event.y
        self.desenhar_figura()
        # Desenha o retângulo temporário (pontilhado) enquanto arrasta
        canvas.create_rectangle(self.ini_x, self.ini_y, self.fim_x, self.fim_y, dash=(4, 2), outline=self.cor)

    def incluir_figura(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

        if self.incompleta():
            self.desenhar_figura()
            return  # Não desenha se o retângulo for incompleto
    
        self.coordenadas = (self.ini_x, self.ini_y, self.fim_x, self.fim_y)

        #Guardamos uma tupla contendo: (tipo_da_figura, coordenadas, cor)
        figuras.append(("Retângulo", self.coordenadas, self.cor_contorno, self.cor_preenchimento))
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
        return self.ini_x == self.fim_x and self.ini_y == self.fim_y