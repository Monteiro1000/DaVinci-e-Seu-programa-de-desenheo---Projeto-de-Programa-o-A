from classe_figura import *
from tela_figuras import *


class Linha(Figura):
    def __init__(self):
        super().__init__("Linha", None, None)
        #coordenadas de início e fim da linha separadas em variaveis individuais
        self.ini_x = None
        self.ini_y = None
        self.fim_x = None
        self.fim_y = None
        
        self.coordenadas = (self.ini_x, self.ini_y, self.fim_x, self.fim_y) #coordenadas da linha como tupla

        self.cor = "black"  # Cor padrão da linha

    # Quando o mouse é pressionado
    def inicia_figura(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    # Quando o mouse é movido com o botão pressionado
    def atualiza_figura(self, event):
        self.fim_x = event.x
        self.fim_y = event.y
        self.desenhar_figura()
        canvas.create_line(self.ini_x, self.ini_y, self.fim_x, self.fim_y, dash=(4, 2), fill=self.cor)  # Desenha a linha temporária enquanto o mouse é arrastado
        

    # Quando o mouse é solto
    def incluir_figura(self, event):
        canvas.create_line(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=self.cor)  # Desenha a linha final
        self.coordenadas = (self.ini_x, self.ini_y, self.fim_x, self.fim_y)  # salva as coordenadas da linha como tupla num parametro do objeto linha
        figuras.append((self.coordenadas, self.cor))  # Adiciona a linha à lista de figuras desenhadas

    def desenhar_figura(self):
        if self.incompleta():
            return  # Não desenha se a linha for incompleta
        canvas.delete("all")
        for figura in figuras:
            canvas.create_line(figura[0][0], figura[0][1], figura[0][2], figura[0][3], fill=figura[1])  # Desenha todas as linhas armazenadas na lista de figuras

    def incompleta(self):
        # Verifica se a linha é incompleta (sem comprimento)
        return self.ini_x == self.fim_x and self.ini_y == self.fim_y

