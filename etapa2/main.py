from tkinter import *
from tkinter import ttk
from opcoes import *
from tela import *
from figura import *
from linha import *
from elipse import *
from rabisco import *
from retangulo import *
from circulo import *
from mouse import *

# ******** MAIN ******** #


canvas.bind("<ButtonPress-1>", clique_no_mouse)
canvas.bind("<B1-Motion>", mover_mouse)
canvas.bind("<ButtonRelease-1>", soltar_mouse)

tela.mainloop()
