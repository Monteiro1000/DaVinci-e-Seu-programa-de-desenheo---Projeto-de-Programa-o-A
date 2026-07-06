from Model.figura import *
from View.tela import *
from View.opcoes import *
from View.cores import*

def desenhar_figura():
    canvas.delete("all") # Limpa os rastros antigos

    for figura in figuras:
        if figura[0] == "Linha":
            canvas.create_line(figura[1][0], figura[1][1], figura[1][2], figura[1][3], fill=figura[2])

        elif figura[0] == "Elipse":
            canvas.create_oval(figura[1][0], figura[1][1], figura[1][2], figura[1][3], 
            outline=figura[2], fill=figura[3])
                
        elif figura[0] == "Círculo":
            nome, coordenadas, cor_contorno, cor_preenchimento = figura #separa os dados de circulo
            canvas.create_oval(coordenadas[0]-coordenadas[2], coordenadas[1]-coordenadas[2],
            coordenadas[0]+coordenadas[2], coordenadas[1]+coordenadas[2],
            outline=cor_contorno, fill=cor_preenchimento )

        elif figura[0] == "Rabisco":
            nome, values, cor = figura # separa a variavel em parametros diferentes
            canvas.create_line(values, fill=cor)

        elif figura[0] == "Retângulo":
            canvas.create_rectangle(figura[1][0], figura[1][1], figura[1][2], figura[1][3],
            outline=figura[2], fill=figura[3])

def desenha_temporaria(figura):

    if figura.nome == "Linha":
        canvas.create_line(
                figura.ini_x,
                figura.ini_y,
                figura.fim_x,
                figura.fim_y,
                dash=(4, 2),
                fill=figura.cor
            )
        
    if figura.nome == "Círculo":
        canvas.create_oval(figura.ini_x-figura.raio, figura.ini_y-figura.raio, figura.ini_x+figura.raio, figura.ini_y+figura.raio, dash=(4,2),
                           outline=figura.cor_contorno)
        
    if figura.nome == "Elipse":
        canvas.create_oval(
                figura.ini_x,
                figura.ini_y,
                figura.fim_x,
                figura.fim_y,
                dash=(4, 2),
                outline=figura.cor_contorno
            )
        
    if figura.nome == "Rabisco":
        canvas.create_line(figura.coordenadas, dash=(4, 2), fill=figura.cor)

    if figura.nome == "Retângulo":
        canvas.create_rectangle(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, dash=(4, 2), outline=figura.cor)
