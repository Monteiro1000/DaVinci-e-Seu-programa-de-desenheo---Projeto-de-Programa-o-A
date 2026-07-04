from tkinter import *
from tkinter import ttk
from classe_cores import *
from tela_figuras import *
from classe_figura import *
from classe_linha import *
from classe_elipse import *
from classe_rabisco import *
from classe_retangulo import *
from classe_circulo import *


# ******** MAIN ******** #


canvas.bind("<ButtonPress-1>", clique_no_mouse)
canvas.bind("<B1-Motion>", mover_mouse)
canvas.bind("<ButtonRelease-1>", soltar_mouse)

tela.mainloop()
