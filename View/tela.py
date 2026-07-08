from tkinter import *

class Tela:
 def __init__(self):
  self.tela = Tk()
  self.frame = Frame(self.tela)
  self.canvas = Canvas(self.frame, bg='white', width=1280, height=720) # Canvas para desenho
  self.canvas.grid(row=2, column=1, columnspan=2, padx=10, pady=10)  # Posiciona o canvas na tela
  self.frame.pack()


app_tela = Tela()
tela = app_tela.tela
frame = app_tela.frame
canvas = app_tela.canvas
tela.title("Da Vinci e seu Programa de Pintura") #Título da janela

titulo = Label(
 frame,
 text="Da Vinci e seu Programa de Pintura",
 font=("Arial", 18, "bold"),
 fg= "#1f4e79"

)
titulo.grid(row=0, column=1, columnspan=2, pady=(10, 5))  # Posiciona o título na tela 

instrucoes = Label( #Instruções para o usuário
  frame,
  text=
        "Instruções:\n"
        "1. Selecione a figura desejada,\n"
        "2. Clique no canvas para desenhar a figura,\n"
        "3. Para desenhar linhas, clique e arraste o mouse.\n"
        "4. Para limpar o canvas, selecione a opção 'Limpar'.",
  
  justify=LEFT, #ajusta o texto à esquerda
  font=("Arial", 10),
)

instrucoes.grid(row=1, column=1, columnspan=2, pady=10)  # Posiciona as instruções na tela