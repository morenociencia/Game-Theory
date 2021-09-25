from ast import Str
from tabulate import tabulate
import numpy as np 
from colorama import *

def main():

    init(autoreset=True)
    
    print()
    print()

    print(Style.BRIGHT+Fore.GREEN+"BIENVENIDO A ESTRATEGIAS ESTRICTAMENTE DOMINANTES")
    print()

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
                m[d, c] = float(input("Ingrese el dato de la"+var12+str(d+1)+" en la"+var13 + str(c+1)+": "))

    def solucion(a,b,m,l):
        
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
            
                listamax.append(m[var6,var5])
            
            #Una vez termina el bucle, se accede a la lista y se busca el valor máximo
            
            var7 = max(listamax)

            #Puesto que el orden como están organizados los datos
            #Tambien refleja el número de la fila
            #Se busca la posoción del valor máximo, que indica la fila
            
            var8 = listamax.index(var7)

            #Dicho resultado se almacena en la lista exterior, que almacena el nombre de las filas
        
            l.append(var8)

            #OBSERVACIÓN IMPORTANTE PARA EL JUGADOR 2 SE INVIERTE LOS VALORES a Y b

    def solucion1(l,z):

        #Se comprueba si todas las filas son congruentes
        #Es decir si existe una estrategia estrictamente dominante
        #Se toma un elemento de la lista que va a servir de comparación

        var9 = l[0]
        
        #Se declara una variable que va a definir mas adelante el resultado, un booleano
        
        var10 = z
        
        #Es necesario crear una variable contador que va a estar dentro del ciclo
        
        var11 = 0

        #Se plantea el ciclo

        for i in l:
            
            #Si el aleatorio es igual a cada uno de los miembros
            #El resultado final debe ser un True
            
            if var9==l[var11]:
                var10 = var10*True

            else:
                var10 = var10*False
            
            #Se coloca un contador que va a recorrer la lista
            
            var11 = var11+1
        
        return var10

    def solucion2(var, l,j):

        #Se plantea un condicional que muestre el resultado

        if j==1:
            var11 = " FILA: "

        elif j==2:
            var11 = " COLUMNA: "

        if bool(var) == True:
            print(Style.BRIGHT+Fore.GREEN+"El Jugador "+str(j)+" TIENE una estrategia estrictamente dominante en la"+var11)
            print(Style.BRIGHT+Fore.YELLOW+"    "+str(l[0]))
        
        else:
            print(Style.BRIGHT+Fore.RED+"El Jugador "+str(j)+" NO tiene una estrategia estrictamente dominante: ")


    jugador1()

    a = int(input("Ingrese la cantidad de FILAS de su matriz: "))

    print()

    b = int(input("Ingrese la cantidad de COLUMNAS de su matriz: "))
    
    print()

    m = np.ones((a, b))

    valoresmatriz(a, b, m,1)

    print()

    print("La matriz de pagos es: ")

    print()

    print(m)

    print()
    print()

    jugador2()

    print()

    #Se invirtieron variables
    #Cambiar nombre filas y columnas
    m1 = np.ones((b, a))

    valoresmatriz(b, a, m1,2)

    print()

    print("La matriz de pagos es: ")
    
    print()

    print(m1)

    print()
    print()

    jugador1()

    listafilas = []
    
    solucion(a,b,m,listafilas)

    var10 = solucion1(listafilas,True)

    print()
    print()

    solucion2(var10,listafilas,1)

    print()
    print()

    jugador2()

    listafilas1 = []

    solucion(b,a,m1,listafilas1)

    var12 = solucion1(listafilas1,True)

    print()
    print()

    solucion2(var12,listafilas1,2)

    print()
    print()

    input()

if __name__ == "__main__":
    main()



