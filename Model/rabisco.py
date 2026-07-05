from Model.figura import *
from View.tela import *
from View.opcoes import *
from View.cores import*

class Rabisco(Figura):

    def __init__(self):
        super().__init__(nome="Rabisco", coordenadas=None, 
        cor=cor_figura_var_contorno.get())
        # inicia a classe Rabisco ja selecionando a cor escolhida

    def inicia_figura(self, event):
        self.coordenadas= [(event.x, event.y)]

    def atualiza_figura(self, event):
        self.coordenadas.append((event.x, event.y))
        canvas.create_line(self.coordenadas, dash=(4, 2), fill=self.cor)
    
    def incluir_figura(self, event):
        if self.incompleta():
            return # Não desenha se o rabisco for incompleto
        figuras.append((self.nome,self.coordenadas, self.cor))  # Adiciona o rabisco à lista de figuras desenhadas
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
        return len(self.coordenadas)  <= 1

