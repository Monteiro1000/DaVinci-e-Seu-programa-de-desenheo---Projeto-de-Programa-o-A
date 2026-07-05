from tkinter import ttk
from View.tela import *
from Model.figura import *

class OpcoesFiguras:
    def __init__(self):
            self.nome = "OpcoesFiguras"
            pass

    def option_menu_desenhos(self):
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

opcoes_figuras = OpcoesFiguras()
opcoes_figuras.option_menu_desenhos()




        
        

            