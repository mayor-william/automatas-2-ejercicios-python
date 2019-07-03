# saber que triangulo es


#funcion para identificar triangulo

def identificar(l1,l2,l3):
    if(l1 == l2 and l1 == l3):
        print(" el triangulo es equilatero: ", l1, ",", l2, ",", l3 )
    elif (l1==l2 or l1==l3 or l2==l3 ):
        print(" el triangulo es isoceles: ", l1, ",", l2, ",", l3)
    elif(l1!=l2 or l1!=l3 or l2!=l3):
        print(" el triangulo es escaleno: ", l1, ",", l2, ",", l3)




def main():
    ciclo = True

    while ciclo == True:
        lado1 = float(input("ingrese el primer lado"))
        lado2 = float(input("ingrese el segundo lado"))
        lado3 = float(input("ingrese el tercer lado"))

        #invocar funcion
        identificar(lado1,lado2,lado3)

        resp = input("Desea hacer otro calculo: (s/n)?")
        if (resp == "S" or resp == "s"):
            ciclo = True
        else:
            ciclo = False
    else:
        print("FIN DEL PROGRAMA")



if __name__ == "__main__":
        main()