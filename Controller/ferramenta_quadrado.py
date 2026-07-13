from Controller.ferramenta import *
from Model.quadrado import *

@dataclass
class Quadrado_Ferramenta(Ferramenta):
    quadrado_novo : Quadrado = None

    def mouse_pressionado(self,event):
        self.quadrado_novo = Quadrado(cor_figura_var_contorno.get(),cor_figura_var_preenchimento.get())
        self.quadrado_novo.inicia_figura(event)
        
    def mouse_arrastado(self,event):
        self.quadrado_novo.atualiza_figura(event)
        desenhador.desenhar_figura()
        if not self.quadrado_novo.incompleta():# não permite figuras temporarias continuarem na tela se forem incompletas
            desenhador.desenha_temporaria(self.quadrado_novo)
        


    def mouse_solto(self,event):
        if not self.quadrado_novo.incompleta(): # para evitar incluir figuras incompletas (vazias)
            self.quadrado_novo.incluir_figura(event)
            desenhador.desenhar_figura()