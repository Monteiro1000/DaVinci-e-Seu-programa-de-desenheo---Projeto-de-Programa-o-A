from Controller.ferramenta import *
from Model.elipse import *

@dataclass
class Elipse_Ferramenta(Ferramenta):
    elipse_nova : Elipse = None

    def mouse_pressionado(self,event):
        self.elipse_nova = Elipse(cor_figura_var_contorno.get(),cor_figura_var_preenchimento.get())
        self.elipse_nova.inicia_figura(event)
        
    def mouse_arrastado(self,event):
        self.elipse_nova.atualiza_figura(event)
        desenhador.desenhar_figura()
        if not self.elipse_nova.incompleta(): # não permite figuras temporarias continuarem na tela se forem incompletas
            desenhador.desenha_temporaria(self.elipse_nova)
            


    def mouse_solto(self,event):
        if not self.elipse_nova.incompleta(): # para evitar incluir figuras incompletas (vazias)
            self.elipse_nova.incluir_figura(event)
            desenhador.desenhar_figura()