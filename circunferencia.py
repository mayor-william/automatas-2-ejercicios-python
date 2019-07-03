# Nombre: circunferencia.py
#Objetivo; calcula el area y diametro de una circunferencia e importar la libreria math
# Autor; memo 2019
#Fecha :1 de julio del 2019

import math as mat
#Funcion para calcular area

def calcularArea(r):
    area = mat.pi *(mat.pow(r,2))
    return area


#funcion para calcular diametro
def calculaDiametro(d):
    diam = d * 2
    return diam


def main():
    ciclo = True
    while ciclo == True:
        print("--Script para calcular el area de una circunferencia --")
        radio = float (input("introduce el valor del radio: "))
        #invocar un metodo
        print("El area es :  ", calcularArea(radio))
        print("El diametro es : " , calculaDiametro(radio))

        resp = input("Desea hacer otro calculo: (s/n)?")
        if(resp == "S" or resp == "s"):
            ciclo = True
        else:
            ciclo = False
    else:
        print("FIN DEL PROGRAMA")



if __name__ == "__main__":
        main()