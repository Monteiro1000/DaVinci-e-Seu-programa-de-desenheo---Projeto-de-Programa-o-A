import pickle
from Model.figura import *
from tkinter import messagebox

class Arquivo:
    def __init__(self):
        self.nome = "Arquivo"

    def salvar_arquivo(self, caminho):
        try:
            with open(caminho, "wb") as arquivo_binario:
                pickle.dump(figuras, arquivo_binario)
            return True
        except Exception as erro:
            messagebox.showerror("Erro ao salvar", f"Não foi possível salvar o arquivo:\n{erro}")
            return False
        
    def abrir_arquivo(self, caminho):
        try:
            with open(caminho, "rb") as arquivo_binario:
                dados = pickle.load(arquivo_binario)
        except Exception as erro:
            messagebox.showerror("Erro ao abrir", f"Não foi possível abrir o arquivo:\n{erro}")
    
        figuras.clear()
        figuras.extend(dados)

        return True  
 

arquivo = Arquivo()