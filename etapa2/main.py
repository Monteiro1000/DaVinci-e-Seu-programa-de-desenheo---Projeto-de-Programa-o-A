from tkinter import *
from tela_figuras import *
from classe_figura import *
from classe_linha import *
from tkinter import ttk
from classe_rabisco import *


#******* MAIN *******#

figura = Linha()  # Inicializa a figura como uma linha

def  option_menu_desenhos(): #função para criar o option menu de desenhos
    label = Label(frame, text="")
    label.grid(column=0, row=0, sticky=NW, padx=15, pady=15)
    descricao_opcao_figura = Label(frame, text="Tipo de figura:") # Label para o option menu de figuras
    descricao_opcao_figura.grid(column=0, row=0, sticky=NW, padx=8, pady=5)
    global tipo_figura_var
    tipo_figura_var = StringVar(tela) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
    option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                                'Linha', 'Linha', 'Rabisco', 'Círculo', 'Retângulo','Elipse') # valores possíveis do option menu
    option_menu.grid(column=0, row=0, sticky=NW, padx=15, pady=30)

option_menu_desenhos()  # Chama a função para criar o option menu de desenhos

def clique_no_mouse(event):

    def criar_figura():
        if tipo_figura_var.get() == "Linha":
            figura = Linha()
            return figura
        elif tipo_figura_var.get() == "Retângulo":
            figura = figura
            return figura
        elif tipo_figura_var.get() == "Rabisco":
            figura = Rabisco()
            return figura
    
    def iniciar_figura(event):
        figura.inicia_figura(event)
    
    criar_figura()  # Cria a figura com base na seleção do option menu
    iniciar_figura(event)  # Inicia a figura com base no evento do clique do mouse

canvas.bind('<ButtonPress-1>', clique_no_mouse)
canvas.bind('<B1-Motion>', figura.atualiza_figura)
canvas.bind('<ButtonRelease-1>', figura.incluir_figura)



tela.mainloop()
