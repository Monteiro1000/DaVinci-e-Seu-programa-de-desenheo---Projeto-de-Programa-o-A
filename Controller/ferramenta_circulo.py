from Controller.ferramenta import *
from Model.circulo import *

@dataclass
class Circulo_Ferramenta(Ferramenta):
    circulo_novo : Circulo = None

    def mouse_pressionado(self,event):
        self.circulo_novo = Circulo(cor_figura_var_contorno.get(),cor_figura_var_preenchimento.get())
        self.circulo_novo.inicia_figura(event)
        
    def mouse_arrastado(self,event):
        self.circulo_novo.atualiza_figura(event)
        desenhador.desenhar_figura()
        if not self.circulo_novo.incompleta(): # não permite figuras temporarias continuarem na tela se forem incompletas
            desenhador.desenha_temporaria(self.circulo_novo)


    def mouse_solto(self,event):
        if not self.circulo_novo.incompleta(): # para evitar incluir figuras incompletas (vazias)
            self.circulo_novo.incluir_figura(event)
            desenhador.desenhar_figura()