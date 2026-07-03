from tkinter import *





figuras = []  # Lista para armazenar todas as figuras desenhadas
tela = Tk()
frame = Frame(tela)
canvas = Canvas(frame, bg='white', width=1280, height=720) # Canvas para desenho
canvas.grid(row=0, column=0, columnspan=2, padx=15, pady=60)  # Posiciona o canvas na tela
frame.pack()
