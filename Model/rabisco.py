from Model.figura import *

class Rabisco(Figura):

    def __init__(self, cor):
        super().__init__(nome="Rabisco", coordenadas=None, 
        cor= cor)
        # inicia a classe Rabisco ja selecionando a cor escolhida

    def inicia_figura(self, event):
        self.coordenadas= [(event.x, event.y)]

    def atualiza_figura(self, event):
        self.coordenadas.append((event.x, event.y))
    
    def incluir_figura(self, event):
        if self.incompleta():
            return # Não desenha se o rabisco for incompleto
        figuras.append((self.nome,self.coordenadas, self.cor))  # Adiciona o rabisco à lista de figuras desenhadas


    def incompleta(self):
        return len(self.coordenadas)  <= 1

