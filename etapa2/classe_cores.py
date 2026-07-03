from tkinter import *
from tkinter import ttk
from classe_figura import *

descricao_opcao_cor_contorno = Label(frame, text="Cor do contorno:") # Label para o option menu de cores
descricao_opcao_cor_contorno.grid(column=0, row=0, sticky=N, padx=0, pady=0)
cor_figura_var_contorno = StringVar(root) # Guarda a cor da figura selecionada
option_menu2 = ttk.OptionMenu(frame, cor_figura_var_contorno,
                               'Preto', 'Preto', 'Branco', 'Vermelho', 'Verde', 'Azul','Nenhum'
                             ) # valores possíveis do option menu de cores para contorno
option_menu2.grid(column=0, row=0, sticky=S, padx=5, pady=5)

# option menu cores preenchimento
descricao_opcao_cor_preenchimento = Label(frame, text="Cor do preenchimento:") # Label para o option menu de cores para preenchimento
descricao_opcao_cor_preenchimento.grid(column=1, row=0, sticky=NW, padx=0, pady=0)
cor_figura_var_preenchimento = StringVar(root) # Guarda a cor da figura selecionada para preenchimento
option_menu3 = ttk.OptionMenu(frame, cor_figura_var_preenchimento,
                               'Nenhum','Nenhum', 'Preto', 'Vermelho', 'Verde', 'Azul', 'Branco'
                             ) # valores possíveis do option menu de cores para preenchimento
option_menu3.grid(column=1, row=0, sticky=SW, padx=35, pady=5)