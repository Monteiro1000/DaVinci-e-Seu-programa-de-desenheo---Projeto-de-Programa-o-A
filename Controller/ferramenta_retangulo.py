from Controller.ferramenta import *
from Model.retangulo import *

@dataclass
class Retangulo_Ferramenta(Ferramenta):
    retangulo_novo : Retangulo = None

    def mouse_pressionado(self,event):
        self.retangulo_novo = Retangulo(cor_figura_var_contorno.get(), cor_figura_var_preenchimento.get())
        self.retangulo_novo.inicia_figura(event)
        
    def mouse_arrastado(self,event):
        self.retangulo_novo.atualiza_figura(event)
        desenhador.desenhar_figura()
        if not self.retangulo_novo.incompleta():# não permite figuras temporarias continuarem na tela se forem incompletas
            desenhador.desenha_temporaria(self.retangulo_novo)


    def mouse_solto(self,event):
        if not self.retangulo_novo.incompleta(): # para evitar incluir figuras incompletas (vazias)
            self.retangulo_novo.incluir_figura(event)
            desenhador.desenhar_figura()