from classe_cores import *
from tela_figuras import *
from classe_figura import *
from classe_linha import *
from classe_elipse import *
from classe_rabisco import *
from classe_retangulo import *
from classe_circulo import *

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