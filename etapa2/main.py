from tkinter import *
from tela_figuras import *
from classe_figura import *
from classe_linha import *

#******* MAIN *******#

figura = Figura('Linha', None, None)  # Instancia a classe base Figura para poder chamar os métodos de desenho
if figura.nome == "Linha":
    figura = Linha()  # Instancia a classe Linha se o nome da figura for "Linha"

canvas.pack()
canvas.bind('<ButtonPress-1>', figura.inicia_figura)
canvas.bind('<B1-Motion>', figura.atualiza_figura)
canvas.bind('<ButtonRelease-1>', figura.incluir_figura)

tela.mainloop()
