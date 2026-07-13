from Controller.ferramenta import *
from Model.rabisco import *

@dataclass
class Rabisco_Ferramenta(Ferramenta):
    rabisco_novo : Rabisco = None

    def mouse_pressionado(self,event):
        self.rabisco_novo = Rabisco(cor_figura_var_contorno.get())
        self.rabisco_novo.inicia_figura(event)
        
    def mouse_arrastado(self,event):
        self.rabisco_novo.atualiza_figura(event)
        desenhador.desenhar_figura()
        if not self.rabisco_novo.incompleta():# não permite figuras temporarias continuarem na tela se forem incompletas
            desenhador.desenha_temporaria(self.rabisco_novo)
        


    def mouse_solto(self,event):
        if not self.rabisco_novo.incompleta(): # para evitar incluir figuras incompletas (vazias)
            self.rabisco_novo.incluir_figura(event)
            desenhador.desenhar_figura()