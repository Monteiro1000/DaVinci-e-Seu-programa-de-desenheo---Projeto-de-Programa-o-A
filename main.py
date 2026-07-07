from tkinter import *
from tkinter import ttk
from View.opcoes import *
from View.tela import *
from View.desenha import *
from View.cores import *
from Model.linha import *
from Controller.mouse import *

# ******** MAIN ******** #
desenhador = Desenha(canvas)
mouse_controller = Mouse(canvas, desenhador, tipo_figura_var)


tela.mainloop()
