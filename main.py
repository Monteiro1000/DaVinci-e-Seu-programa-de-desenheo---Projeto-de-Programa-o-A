import testetkinter


#*** MAIN ***#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame

paddings = {'padx': 5, 'pady': 5} #padding usado com a formatacao anterior do grid 

# padding usado com a formatacao atual do grid, serve para espacar a parte de cima, sem mecher nos paddings dos outros widgets
label = Label(frame, text="")
label.grid(column=0, row=0, sticky=W, padx=15, pady=15)




# option menu desenhos
descricao_opcao_figura = Label(frame, text="Tipo de figura:") # Label para o option menu de figuras
descricao_opcao_figura.grid(column=0, row=0, sticky=NW, padx=0, pady=0)
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Círculo', 'Retângulo','Elipse') # valores possíveis do option menu
option_menu.grid(column=0, row=0, sticky=SW, padx=8, pady=5)

# option menu cores
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

# Área de desenho
canvas = Canvas(frame, bg='white', width=1280, height=720) # canvas para desenho
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()