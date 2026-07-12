from Model.arquivo import arquivo
from View.desenha import *
from tkinter import filedialog

class Salvar_Abrir:
    def __init__(self):
        self.nome = "Salvar_Abrir"
    
    def salvar_desenho(self):
        caminho = filedialog.asksaveasfilename(
            title = "Salvar desenho",
            defaultextension = ".davinci",
            filetypes = [("Arquivo de desenho (Da Vinci)", "*.davinci")]
        )
        
        if not caminho:
            return
        
        arquivo.salvar_arquivo(caminho)
    
    def abrir_desenho(self):
        caminho = filedialog.asksaveasfilename(
            title = "Abrir desenho",
            filetypes = [("Arquivo de desenho (Da Vinci)", "*.davinci")]
     
        )

        if not caminho:
            return  # usuário cancelou o diálogo

        if arquivo.abrir_arquivo(caminho):
            desenhador.desenhar_figura()

Salvar_Abrir = Salvar_Abrir()