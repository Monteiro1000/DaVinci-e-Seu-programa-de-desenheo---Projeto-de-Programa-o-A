from abc import abstractmethod, ABC

figuras = []  # Lista para armazenar todas as figuras desenhadas
class Figura(ABC):
    #classe base para todas as figuras geométricas
    def __init__(self,nome,coordenadas,cor):
        self.nome = nome
        self.coordenadas = coordenadas
        self.cor = cor
    
    # Quando o mouse é pressionado
    @abstractmethod
    def inicia_figura(self, event):
        pass

    # Quando o mouse é movido com o botão pressionado
    @abstractmethod
    def atualiza_figura(self, event):
        pass
        

    # Quando o mouse é solto
    @abstractmethod
    def incluir_figura(self, event):
        pass

