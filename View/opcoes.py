from tkinter import ttk
from View.tela import *
from Model.figura import *
from tkinter import Button
from Controller.salvar_abrir import Salvar_Abrir

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
            "Quadrado",
            "Elipse",
            "Selecionar",
        )

        option_menu.grid(column=0, row=0, sticky=NW, padx=4, pady=25)

botao_limpar = Button(
     frame,
     text='Limpar',
        command=lambda: [figuras.clear(), canvas.delete("all")],  # Limpa o canvas e a lista de figuras
        bg='red',
        fg='white',
        font=("Arial", 10, "bold")
)
botao_limpar.grid(column=0, row=10, sticky=EW, padx=10, pady=10)



botao_salvar = Button(
     frame,
     text='Salvar',
        command=lambda: Salvar_Abrir.salvar_desenho (),  
        bg='blue',
        fg='white',
        font=("Arial", 10, "bold")
)
botao_salvar.grid(column=0, row=11, sticky=EW, padx=10, pady=5)


botao_abrir = Button(
     frame,
     text='Abrir',
        command=lambda: Salvar_Abrir.abrir_desenho (), 
        bg='blue',
        fg='white',
        font=("Arial", 10, "bold")
)
botao_abrir.grid(column=0, row=12, sticky=EW, padx=10, pady=5)

opcoes_figuras = OpcoesFiguras()
opcoes_figuras.option_menu_desenhos()



        
        

            