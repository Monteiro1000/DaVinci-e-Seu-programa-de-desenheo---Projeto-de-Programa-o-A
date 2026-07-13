from Controller.ferramenta import *
from Model.linha import *

@dataclass
class Linha_Ferramenta(Ferramenta):
    linha_nova : Linha = None

    def mouse_pressionado(self,event):
        self.linha_nova = Linha(cor_figura_var_contorno.get())
        self.linha_nova.inicia_figura(event)
        
    def mouse_arrastado(self,event):
        self.linha_nova.atualiza_figura(event)
        desenhador.desenhar_figura() 
        if not self.linha_nova.incompleta(): # não permite figuras temporarias continuarem na tela se forem incompletas
            desenhador.desenha_temporaria(self.linha_nova)


    def mouse_solto(self,event):
        if not self.linha_nova.incompleta(): # para evitar incluir figuras incompletas (vazias)
            self.linha_nova.incluir_figura(event)
            desenhador.desenhar_figura()