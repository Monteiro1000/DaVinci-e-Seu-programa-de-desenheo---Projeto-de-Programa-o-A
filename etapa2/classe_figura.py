class Figura:
    #classe base para todas as figuras geométricas
    def __init__(self,nome,coordenadas,cor):
        self.nome = nome
        self.coordenadas = coordenadas
        self.cor = cor

    # Quando o mouse é pressionado
    def inicia_figura(self, event):
        pass

    # Quando o mouse é movido com o botão pressionado
    def atualiza_figura(self, event):
        pass
        

    # Quando o mouse é solto
    def incluir_figura(self, event):
        pass

    # Desenha a figura no canvas
    def desenhar_figura(self):
        pass

