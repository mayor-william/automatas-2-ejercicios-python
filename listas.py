# Nombre: listas.py
# Objetivo: muestra el funcionamiento de las listas en python
# Autor: Guillermo Eduardo Granados Davalos
# Fecha: 02 Julio de 2019


#  crear la lista

lista = []


# Funcion para agregar items a la lista
def agregarItem(dato):
    lista.append(dato)


def buscarDato(dato):
    if (dato in lista):

        print(dato)
    else:
        print("el dato no existe en la lista")


def eliminarItem(dato):
    if (dato in lista):
        lista.remove(dato)
        print("dato eliminado")
    else:
        print("el dato no existe en la lista")


#imprimir lista
def imprimirLista():
    j = 1
    for i in lista:
        print("ITEM: ", j, ",", i)
        j = j + 1


def main():
    ciclo = True
    while (ciclo == True):


        opcion = int(input("1 para agregar elemento, 2 para buscar, 3 para modificar, 4 para eliminar, 5 imprimir, 6 salir"))

        if (opcion == 1):
            dato = input("ingrese el dato que quiera ")
            agregarItem(dato)
        elif (opcion == 2):
            buscar = input("ingrese el dato que busca")
            buscarDato(buscar)


        elif (opcion == 3):
            print("opcion3")


        elif (opcion == 4):
            eliminar = input("eliminar un dato")
            eliminarItem(eliminar)

        elif (opcion == 5):
            imprimirLista()

        elif (opcion == 6):
            ciclo = False
            print("fin del programa")

        else:
            print(" nomas puedes poner numeros del 1 al 6")






if __name__ == '__main__':
        main()