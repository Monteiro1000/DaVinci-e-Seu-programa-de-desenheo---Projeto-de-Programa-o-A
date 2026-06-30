from tkinter import *
from tkinter import ttk

dicionario_cores = {'Preto': 'black', 'Branco': 'white', 'Vermelho': 'red', 'Verde': 'green', 'Azul': 'blue','Nenhum': ''   }

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y))
    elif tipo_figura_var.get() == 'Rabisco':
        figura_nova = ["rabisco", [(event.x, event.y)],dicionario_cores[cor_figura_var_contorno.get()]] # (x1, y1, x2, y2)
    elif tipo_figura_var.get() == 'Círculo':
        figura_nova = ("círculo", (event.x, event.y, 0)) # (x_centro, y_centro, raio)
    elif tipo_figura_var.get() == 'Retângulo':
        figura_nova = ("retângulo", (event.x, event.y, event.x, event.y)) # (x1, y1, x2, y2)
    elif tipo_figura_var.get() == 'Elipse':
        figura_nova = ("elipse", (event.x, event.y, 0,0)) # (x1, y1, x2, y2)


# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "círculo":
        figura_nova = ("círculo", (figura_nova[1][0], figura_nova[1][1], ((event.x - figura_nova[1][0])**2 + (event.y - figura_nova[1][1])**2)**0.5, dicionario_cores[cor_figura_var_contorno.get()], dicionario_cores[cor_figura_var_preenchimento.get()]))
    elif figura_nova[0] == "linha":
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y,dicionario_cores[cor_figura_var_contorno.get()]))
    elif figura_nova[0] == "retângulo":
        figura_nova = ("retângulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y,dicionario_cores[cor_figura_var_contorno.get()],dicionario_cores[cor_figura_var_preenchimento.get()]))
    elif figura_nova[0] == "elipse":
        figura_nova = ("elipse", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
        raio_x = (event.x - figura_nova[1][0])
        raio_y = (event.y - figura_nova[1][1])
        figura_nova = ("elipse", (figura_nova[1][0], figura_nova[1][1],raio_x, raio_y,dicionario_cores[cor_figura_var_contorno.get()],dicionario_cores[cor_figura_var_preenchimento.get()]))
    desenhar_figuras()
    desenhar_figura_nova()


# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()


def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras:
        if figura[0] == "rabisco":
            nome, values, cor = figura
            canvas.create_line(values, fill=cor)
        else:
            fig, values = figura
            if fig == "linha":
                canvas.create_line(values[0], values[1], values[2], values[3], fill=values[4])
            elif fig == "círculo":
                canvas.create_oval(values[0] - values[2], values[1] - values[2], values[0] + values[2], values[1] + values[2],outline=values[3], fill=values[4])
            elif fig == "retângulo":   
                canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=values[4], fill=values[5])
            elif fig == "elipse":
                canvas.create_oval(values[0] - values[2], values[1] - values[3], values[0] + values[2], values[1] + values[3], outline=values[4], fill=values[5])

def desenhar_figura_nova():
    if figura_nova[0] == "rabisco":
        nome, values, cor = figura_nova
        canvas.create_line(values, dash=(4, 2), fill=cor)
    else:
        fig, values = figura_nova
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=values[4])
        elif fig == "círculo":
            canvas.create_oval(values[0] - values[2], values[1] - values[2], values[0] + values[2], values[1] + values[2], dash=(4, 2))
        elif fig == "retângulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2))
        elif fig == "elipse":
            canvas.create_oval(values[0] - values[2], values[1] - values[3], values[0] + values[2], values[1] + values[3], dash=(4, 2))

def incompleta(figura):
    if figura[0] == "rabisco":
        return len(figura[1]) <= 1
    fig, values = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "círculo":
        return values[2] == 0
    elif fig == "retângulo":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "elipse":
        return values[2] == 0 or values[3] == 0

