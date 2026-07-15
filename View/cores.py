from tkinter import ttk
from View.tela import *
from Model.figura import *



# criacao de variaveis globais para declaracao das cores em cada figura
cor_figura_var_contorno = StringVar()
cor_figura_var_contorno.set("black") #define a cor padrao do contorno
cor_figura_var_preenchimento = StringVar()
cor_figura_var_preenchimento.set("")#define a cor padrao do preencimento
preenchimento = StringVar()
contorno = StringVar()
preenchimento.set("False")#define o preenchimento como desativado por padrao
contorno.set("True")#define o contorno como ativado por padrao

class Cores:

    def __init__(self):
        self.nome = "classe cores"
        pass

    # Aplica a cor escolhida na figura atualmente selecionada, se houver.
    def aplica_cor_selecionada(self, cor):
        from Controller.mouse import mouse_controller
        if getattr(mouse_controller, "figura_selecionada", None) is None:
            return

        indice = mouse_controller.figura_selecionada
        if indice is None or indice >= len(figuras):
            return

        figura = list(figuras[indice])
        nome = figura[0]

        if contorno.get() == "True":
            if nome in {"Linha", "Rabisco"}:
                figuras[indice] = (nome, figura[1], cor)
            elif len(figura) >= 4:
                figuras[indice] = (nome, figura[1], cor, figura[3])

        if preenchimento.get() == "True" and nome in {"Elipse", "Círculo", "Retângulo", "Quadrado"} and len(figura) >= 4:
            figuras[indice] = (nome, figura[1], figura[2], cor)

        desenhador.desenhar_figura()

    # Funcao que define se o botao de preenchimento esta apertado
    def aperta_preenchimento(self):
        if preenchimento.get() == "False":
            preenchimento.set("True")
            self.botao_preenchimento.configure(bg="green")

        else:
            preenchimento.set("False")
            self.botao_preenchimento.configure(bg="white")
    
    # Funcao que define se o botao de contorno esta apertado
    def aperta_contorno(self):
        if contorno.get() == "False":
            contorno.set("True")
            self.botao_contorno.configure(bg="green")

        else:
            contorno.set("False")
            self.botao_contorno.configure(bg="white")




    #layout do botao de preenchimento
    botao_preenchimento = Button(frame,text="Preenchimento",bg="white",command= lambda: cores.aperta_preenchimento())
    botao_preenchimento.grid(column=0,row=0,padx=0,pady=0)
    botao_preenchimento.place(x=7, y =300)

    #layout do botao de contorno
    botao_contorno = Button(frame,text="contorno",bg="green",command= lambda: cores.aperta_contorno())
    botao_contorno.grid(column=0,row=0,padx=0,pady=0)
    botao_contorno.place(x=7, y =330)

    #Armazena os botoes de cores e seus respectivos dados

    def botao_black_aperta(self): # define o que o botao preto faz quando pressionado
        if contorno.get() == "True":
            cor_figura_var_contorno.set("black")
        if preenchimento.get() == "True":
            cor_figura_var_preenchimento.set('black')
        self.aplica_cor_selecionada("black")
        return cor_figura_var_contorno and cor_figura_var_preenchimento


    #layout do botao preto
    botao_black= Button(frame,text="     ",bg="black",command= lambda: cores.botao_black_aperta())
    botao_black.grid(column=0,row=0,padx=0,pady=0)
    botao_black.place(x=7, y =400)


    def botao_gray_aperta(self): # define o que o botao cinza faz quando pressionado
        if contorno.get() == "True":
            cor_figura_var_contorno.set("gray")
        if preenchimento.get() == "True":
            cor_figura_var_preenchimento.set('gray')
        self.aplica_cor_selecionada("gray")
        return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout botao cinza
    botao_gray = Button(frame,text="     ",bg="gray",command= lambda: cores.botao_gray_aperta())
    botao_gray.grid(column=0,row=0,padx=0)
    botao_gray.place(x=36,y =400)

    def botao_white_aperta(self): # define o que o botao branco faz quando pressionado
            if contorno.get() == "True":
                cor_figura_var_contorno.set("white")
            if preenchimento.get() == "True":
                cor_figura_var_preenchimento.set('white')
            self.aplica_cor_selecionada("white")
            return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout botao branco
    botao_white= Button(frame,text="     ",bg="white", command= lambda: cores.botao_white_aperta())
    botao_white.grid(column=0,row=0,padx=0)
    botao_white.place(x=65, y =400)

    def botao_red_aperta(self): # define o que o botao red faz quando pressionado
            if contorno.get() == "True":
                cor_figura_var_contorno.set("red")
            if preenchimento.get() == "True":
                cor_figura_var_preenchimento.set('red')
            self.aplica_cor_selecionada("red")
            return cor_figura_var_contorno and cor_figura_var_preenchimento
    
    #layout botao vermelho
    botao_red = Button(frame,text="     ",bg="red",command= lambda: cores.botao_red_aperta())
    botao_red.grid(column=0,row=0,padx=0)
    botao_red.place(x=7, y =430)


    def botao_blue_aperta(self): # define o que o botao azul faz quando pressionado
            if contorno.get() == "True":
                cor_figura_var_contorno.set("blue")
            if preenchimento.get() == "True":
                cor_figura_var_preenchimento.set('blue')
            self.aplica_cor_selecionada("blue")
            return cor_figura_var_contorno and cor_figura_var_preenchimento
    

    #layout botao azul
    botao_blue= Button(frame,text="     ",bg="blue", command= lambda: cores.botao_blue_aperta())
    botao_blue.grid(column=0,row=0,padx=0)
    botao_blue.place(x=36,y =430)

    def botao_green_aperta(self): # define o que o botao verde faz quando pressionado
            if contorno.get() == "True":
                cor_figura_var_contorno.set("green")
            if preenchimento.get() == "True":
                cor_figura_var_preenchimento.set('green')
            self.aplica_cor_selecionada("green")
            return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout botao verde
    botao_green= Button(frame,text="     ",bg="green",command= lambda: cores.botao_green_aperta() )
    botao_green.grid(column=0,row=0,padx=0)
    botao_green.place(x=65, y =430)

    def botao_yellow_aperta(self): # define o que o botao amarelo faz quando pressionado
            if contorno.get() == "True":
                cor_figura_var_contorno.set("yellow")
            if preenchimento.get() == "True":
                cor_figura_var_preenchimento.set('yellow')
            self.aplica_cor_selecionada("yellow")
            return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout botao amarelo
    botao_yellow= Button(frame,text="     ",bg="yellow", command= lambda: cores.botao_yellow_aperta())
    botao_yellow.grid(column=0,row=0,padx=0)
    botao_yellow.place(x=7, y =460)

    def botao_pink_aperta(self): # define o que o botao rosa faz quando pressionado
            if contorno.get() == "True":
                cor_figura_var_contorno.set("pink")
            if preenchimento.get() == "True":
                cor_figura_var_preenchimento.set('pink')
            self.aplica_cor_selecionada("pink")
            return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout botao rosa
    botao_pink= Button(frame,text="     ",bg="pink",command= lambda: cores.botao_pink_aperta() )
    botao_pink.grid(column=0,row=0,padx=0)
    botao_pink.place(x=36,y =460)

    def botao_light_blue_aperta(self): # define o que o botao azul claro faz quando pressionado
                if contorno.get() == "True":
                    cor_figura_var_contorno.set("lightblue")
                if preenchimento.get() == "True":
                    cor_figura_var_preenchimento.set('lightblue')
                self.aplica_cor_selecionada("lightblue")
                return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout botao azul claro
    botao_light_blue = Button(frame,text="     ",bg="lightblue",command= lambda: cores.botao_light_blue_aperta() )
    botao_light_blue.grid(column=0,row=0,padx=0)
    botao_light_blue.place(x=65, y =460)

    def botao_purple_aperta(self): # define o que o botao roxo faz quando pressionado
                if contorno.get() == "True":
                    cor_figura_var_contorno.set("purple")
                if preenchimento.get() == "True":
                    cor_figura_var_preenchimento.set('purple')
                self.aplica_cor_selecionada("purple")
                return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout do botao roxo
    botao_purple = Button(frame,text="     ",bg="purple",command= lambda: cores.botao_purple_aperta() )
    botao_purple.grid(column=0,row=0,padx=0)
    botao_purple.place(x=7, y =490)

    def botao_brown_aperta(self): # define o que o botao marrom faz quando pressionado
                if contorno.get() == "True":
                    cor_figura_var_contorno.set("brown")
                if preenchimento.get() == "True":
                    cor_figura_var_preenchimento.set('brown')
                self.aplica_cor_selecionada("brown")
                return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout do botao marrom
    botao_brown =Button(frame,text="     ",bg="brown",command= lambda: cores.botao_brown_aperta())
    botao_brown.grid(column=0,row=0,padx=0)
    botao_brown.place(x=36, y =490)

    def botao_orange_aperta(self): # define o que o botao laranja faz quando pressionado
                if contorno.get() == "True":
                    cor_figura_var_contorno.set("orange")
                if preenchimento.get() == "True":
                    cor_figura_var_preenchimento.set('orange')
                self.aplica_cor_selecionada("orange")
                return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout do botao laranja
    botao_orange = Button(frame,text="     ",bg="orange", command= lambda: cores.botao_orange_aperta())
    botao_orange.grid(column=0,row=0,padx=0,pady=0)
    botao_orange.place(x=65, y =490)

    def botao_sem_cor_aperta(self): # define o que o botao sem cor faz quando pressionado
                if contorno.get() == "True":
                     cor_figura_var_contorno.set("")
                if preenchimento.get() == "True":
                    cor_figura_var_preenchimento.set('')
                self.aplica_cor_selecionada("")
                return cor_figura_var_contorno and cor_figura_var_preenchimento

    #layout do botao sem cor
    botao_sem_cor = Button(frame,text="Sem Cor", command= lambda: cores.botao_sem_cor_aperta())
    botao_sem_cor.grid(column=0,row=0,padx=0,pady=0)
    botao_sem_cor.place(x=23, y =520)

cores = Cores()
