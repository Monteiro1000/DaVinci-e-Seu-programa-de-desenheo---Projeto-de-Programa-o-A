from tkinter import *

class Tela:
 def __init__(self):
  self.tela = Tk()
  self.frame = Frame(self.tela)
  self.canvas = Canvas(self.frame, bg='white', width=1280, height=720) # Canvas para desenho
  self.canvas.grid(row=0, column=1, columnspan=2, padx=0, pady=50)  # Posiciona o canvas na tela
  self.frame.pack()


app_tela = Tela()
tela = app_tela.tela
frame = app_tela.frame
canvas = app_tela.canvas
