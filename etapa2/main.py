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

figura = Linha()  # Figura inicial


def option_menu_desenhos():
    """Cria o menu de seleção das figuras."""

    Label(frame, text="").grid(column=0, row=0, sticky=NW, padx=15, pady=15)

    Label(
        frame,
        text="Tipo de figura:"
    ).grid(column=0, row=0, sticky=NW, padx=8, pady=0)

    global tipo_figura_var

    tipo_figura_var = StringVar(tela)
    tipo_figura_var.set("Linha")

    option_menu = ttk.OptionMenu(
        frame,
        tipo_figura_var,
        "Linha",
        "Linha",
        "Rabisco",
        "Círculo",
        "Retângulo",
        "Elipse"
    )

    option_menu.grid(column=0, row=0, sticky=NW, padx=4, pady=25)


option_menu_desenhos()


def criar_figura():

    opcao = tipo_figura_var.get()

    if opcao == "Linha":
        return Linha()

    elif opcao == "Elipse":
        return Elipse()
    
    elif opcao == "Círculo":
        return Circulo()

    elif opcao == "Retângulo":
        return Retangulo()

    elif opcao == "Rabisco":
        return Rabisco()

    return Linha()


def clique_no_mouse(event):

    global figura

    figura = criar_figura()
    figura.inicia_figura(event)


def mover_mouse(event):
    figura.atualiza_figura(event)


def soltar_mouse(event):
    figura.incluir_figura(event)


canvas.bind("<ButtonPress-1>", clique_no_mouse)
canvas.bind("<B1-Motion>", mover_mouse)
canvas.bind("<ButtonRelease-1>", soltar_mouse)

tela.mainloop()
