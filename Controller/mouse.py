from View.opcoes import *
from View.tela import *
from Model.figura import *
from Model.linha import *
from Model.elipse import *
from Model.rabisco import *
from Model.retangulo import *
from Model.circulo import *

figura = Linha()  # Figura inicial


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
