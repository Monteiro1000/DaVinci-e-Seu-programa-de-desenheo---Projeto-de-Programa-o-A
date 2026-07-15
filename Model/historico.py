import copy
from Model.figura import figuras

class Historico:
    def __init__(self):
        self.nome = "Historico"
        self.pilha_undo = [] #empilha os estados salvos das figuras
        self.limite = 50
    
    #salva o estado das figuras"
    def salva_estado(self):
        self.pilha_undo.append(copy.deepcopy(figuras))
        if len(self.pilha_undo) > self.limite:
            self.pilha_undo.pop(0)
            
    #remove o ultimo estado salvo"
    def desfazer(self):
        if not self.pilha_undo:
            return False
        estado_anterior = self.pilha_undo.pop()
        figuras.clear()
        figuras.extend(estado_anterior)
        return True
    
    
historico = Historico()