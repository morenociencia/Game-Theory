import numpy as np 
from colorama import *

init(autoreset=True)

#-------------------------Funciones del modulo------------------------
def jugador1():
        j = " JUGADOR 1 "
        print(Style.BRIGHT+Fore.YELLOW+j.center(80, "%"))
        print()


def jugador2():
        j1 = " JUGADOR 2 "
        print(Style.BRIGHT+Fore.CYAN+j1.center(80, "%"))
        print()


def valoresmatriz(a,b,m,j):
        
        if j==1:
            var12 = " Fila "
            var13 = " Columna "

        elif j==2:
            var12 = " Columna "
            var13 = " Fila "

        for c in range(b):
            
            for d in range(a):

                while True:

                    try:

                        m[d, c] = float(input("Ingrese el dato de la"+var12+str(d+1)+" en la"+var13 + str(c+1)+": "))
                        break
                    
                    except ValueError:

                        print("El valor ingresado es incorrecto.")

        return m


def solucion(a,b,m1,l):

    #Sea b Columnas
    #Se crea bucle for que se repite según columnas.
        
    for var5 in range(b):

        #Se crea una lista vacia que alamacenará temporalmente los valores maximos 
        listamax = []
            
        #Se crea otro bucle for interno
        #Este bucle es de las filas y se repite según las columnas que existan
            
        for var6 in range(a):
            
            #Se agrega a una lista los valores de la fila manteniendo constante la columna
            #Esto se hace porque se está comparando el jugador 1
            
            listamax.append(m1[var6,var5])
            
        #Una vez termina el bucle, se accede a la lista y se busca el valor máximo
            
        var7 = max(listamax)

        #Puesto que el orden como están organizados los datos
        #Tambien refleja el número de la fila
        #Se busca la posoción del valor máximo, que indica la fila
            
        var8 = listamax.index(var7)

        #Dicho resultado se almacena en la lista exterior, que almacena el nombre de las filas
        
        l.append(var8)
    
    return l

    #OBSERVACIÓN IMPORTANTE PARA EL JUGADOR 2 SE INVIERTE LOS VALORES a Y b


def solucion1(l1,z):

    #Se comprueba si todas las filas son congruentes
    #Es decir si existe una estrategia estrictamente dominante
    #Se toma un elemento de la lista que va a servir de comparación

    var9 = l1[0]
        
    #Se declara una variable que va a definir mas adelante el resultado, un booleano
        
    var10 = z
        
    #Es necesario crear una variable contador que va a estar dentro del ciclo
        
    var11 = 0

    #Se plantea el ciclo

    for i in l1:
            
        #Si el aleatorio es igual a cada uno de los miembros
        #El resultado final debe ser un True
            
        if var9==l1[var11]:

            var10 = var10*True

        else:

            var10 = var10*False
            
        #Se coloca un contador que va a recorrer la lista
            
        var11 = var11+1
        
    return var10


def solucion2(var, l1,j):

    #Se plantea un condicional que muestre el resultado

    if j==1:

        var11 = " FILA: "

    elif j==2:

        var11 = " COLUMNA: "

    if bool(var) == True:

        print(Style.BRIGHT+Fore.GREEN+"El Jugador "+str(j)+" TIENE una estrategia estrictamente dominante en la"+var11)
        print(Style.BRIGHT+Fore.YELLOW+"    "+str(l1[0]))
        
    else:
        print(Style.BRIGHT+Fore.RED+"El Jugador "+str(j)+" NO tiene una estrategia estrictamente dominante: ")


def main():

    print()
    print()

    print(Style.BRIGHT+Fore.GREEN+"BIENVENIDO A ESTRATEGIAS ESTRICTAMENTE DOMINANTES")
    print()

    #--------------------Jugador 1
    jugador1()

    while True:

        try:
            
            a = int(input("Ingrese la cantidad de FILAS de su matriz: "))
            1/a
            if a>0:

                break
        
            print("No es un número mayor a cero.")

        except ValueError:

            print("El valor ingresado es erróneo.")

        except ZeroDivisionError:

            print("No puede ser cero.")

    print()

    while True:

        try:
            
            b = int(input("Ingrese la cantidad de COLUMNAS de su matriz: "))
            1/b
            
            if b>0:

                break
            
            print("No es un número mayor a cero.")

        except ValueError:

            print("El valor ingresado es erróneo.")
        
        except ZeroDivisionError:

            print("No puede ser cero.")

    
    print()

    m = np.ones((a, b))

    m1 = valoresmatriz(a, b, m,1)

    print()

    print("La matriz de pagos es: ")

    print()

    print(m1)

    print()
    print()

    #----------------------Jugador 2
    jugador2()

    print()

    #Se invirtieron variables
    #Cambiar nombre filas y columnas
    m2 = np.ones((b, a))

    m3 = valoresmatriz(b, a, m2,2)

    print()

    print("La matriz de pagos es: ")
    
    print()

    print(m3)

    print()
    print()

    #----------------------Jugador 1
    jugador1()

    listafilas = []
    
    listafilas1 = solucion(a,b,m1,listafilas)

    var10 = solucion1(listafilas1,True)

    print()
    print()

    solucion2(var10,listafilas1,1)

    print()
    print()

    #--------------------------Jugador 2
    jugador2()
    
    listafilas2 = []

    solucion(b,a,m3,listafilas2)

    var12 = solucion1(listafilas2,True)

    print()
    print()

    solucion2(var12,listafilas2,2)

    print()
    print()
