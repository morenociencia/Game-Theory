import numpy as np
from colorama import *
#Importando para convertir a fraccionarios decimales
from fractions import Fraction
from string import ascii_letters

def main():

    init(autoreset=True)

    #Creando funciones
    def iniciovariables():
        print("Recuerde que la comparación del JUGADOR 1 se hace en HORIZONTAL")
        print("Recuerde que debe ingresar las probabilidades manualmente ")
        print()
        print("Recuerde que el valor ingresado se le va a sumar 1 por la probabilidad")
        print()
        cantidadvar = int(input("Ingrese la cantidad de filas o columnas: "))
        cantidadvar = cantidadvar+1 
        return cantidadvar

    #Sacando matriz inversa
    def matrizinv(a):
        b = np.linalg.inv(a)
        return b

    #Generando multiplicación de matrices
    def multi(m1,p):
        resultado = np.matmul(m1, p)
        return resultado

    def totaldatos():
        x1 = cantidadvar**(2)
        return x1

    def datos():
        x = int(input("Ingrese un elemento: "))
        return x

    def inicio():
        for contador in range(totaldatos()):
            lista.append(datos())

    #Creando Matriz de probabilidad
    def probabilidad():
        #Creando una matriz identidad a partir de la info aportada por el usuario
        midentidad = np.identity(cantidadvar, dtype=int)
        #Seleccionando ultima fila
        var3 = cantidadvar - 1 
        ultimafila = midentidad[var3 : cantidadvar]
        #Sacando transpuesta para poder realizar la operación
        uftrans = np.transpose(ultimafila)
        return uftrans

    #Conversión de decimales a fracciones
    def frac(var4):
        for i in range(var4):
            var5 = float(resultado[i])
            print(Fraction(var5).limit_denominator())


    print()
    print(Style.BRIGHT+Fore.GREEN+"BIENVENIDO A ESTRATEGIA MIXTA CON MATRICES DE NASH")
    print()

    #Variables que siempre van a estar
    variables = list(ascii_letters) 

    lista = []

    var = None

    cantidadvar = iniciovariables()

    #Limite variables
    if cantidadvar>6:
        print()
        print("El programa actual no soporta la cantidad de variables indicadas")
        input()

    #Si contador es igual a cero, entonces var es igual al primer elemento de la lista
    #cuando contador es distinto de cero, a var que ya es un string se le suman otros string
    #Finalmente se crea una variable que tiene los elementos para crear el diccionario zip
    for var1 in range(totaldatos()):
        if  var1 != 0:
            var = var + (variables[var1])
        elif var1 == 0:
            var = (variables[var1])

    if cantidadvar==2:
            
        inicio()
        print()

        #Se crea un diccionario
        diccionario = dict(zip(var, lista))

        #se crea una matriz cuadrada dependiendo de los datos ingresados, por eso existe el diccionario
        m = np.array([[diccionario["a"],diccionario["b"]],[diccionario["c"],diccionario["d"]]])
        print(m)

        #Sacando matriz inversa
        m1 = matrizinv(m)

        #Creando matriz de probabilidades
        p = probabilidad()

        #Generando multiplicación
        resultado = multi(m1,p)
        print()
            
        print(resultado)

        print()
        print()

        #Mostrando fraccionario
        frac(cantidadvar)

        print()

    elif cantidadvar==3:
        inicio()
        print()
        diccionario = dict(zip(var,lista))

        m = np.array([[diccionario["a"],diccionario["b"],diccionario["c"]],
        [diccionario["d"],diccionario["e"],diccionario["f"]], 
        [diccionario["g"],diccionario["h"],diccionario["i"]]])
        print(m)

        #Sacando matriz inversa
        m1 = matrizinv(m)

        #Creando matriz de probabilidades
        p = probabilidad()

        #Generando multiplicación
        resultado = multi(m1,p)
        print()
            
        print(resultado)

        print()
        print()

        #Mostrando fraccionario
        frac(cantidadvar)

        print()

    elif cantidadvar==4:

        inicio()
        print()
        diccionario = dict(zip(var,lista))

        m = np.array([[diccionario["a"],diccionario["b"],diccionario["c"],diccionario["d"]],
        [diccionario["e"],diccionario["f"], diccionario["g"],diccionario["h"]],
        [diccionario["i"],diccionario["j"],diccionario["k"],diccionario["l"]],
        [diccionario["m"],diccionario["n"],diccionario["o"],diccionario["p"]]])
        print(m)

        #Sacando matriz inversa
        m1 = matrizinv(m)

    #Creando matriz de probabilidades
        p = probabilidad()

        #Generando multiplicación
        resultado = multi(m1,p)
        print()
            
        print(resultado)

        print()
        print()

        #Mostrando fraccionario
        frac(cantidadvar)
            
        print()

    elif cantidadvar==5:
        inicio()
        print()
        diccionario = dict(zip(var,lista))

        m = np.array([[diccionario["a"],diccionario["b"],diccionario["c"],diccionario["d"],diccionario["e"]],
        [diccionario["f"], diccionario["g"],diccionario["h"],diccionario["i"],diccionario["j"]],
        [diccionario["k"],diccionario["l"],diccionario["m"],diccionario["n"],diccionario["o"]],
        [diccionario["p"],diccionario["q"],diccionario["r"],diccionario["s"],diccionario["t"]],
        [diccionario["u"],diccionario["v"],diccionario["w"],diccionario["x"],diccionario["y"]]])
        print(m)

        #Sacando matriz inversa
        m1 = matrizinv(m)

        #Creando matriz de probabilidades
        p = probabilidad()

        #Generando multiplicación
        resultado = multi(m1,p)
        print()
        
        print(resultado)

        print()
        print()

        #Mostrando fraccionario
        frac(cantidadvar)

        print()

    elif cantidadvar==6:
        inicio()
        print()
        diccionario = dict(zip(var,lista))

        m = np.array([[diccionario["a"],diccionario["b"],diccionario["c"],diccionario["d"],diccionario["e"],diccionario["f"]],
        [diccionario["g"],diccionario["h"],diccionario["i"],diccionario["j"],diccionario["k"],diccionario["l"]],
        [diccionario["m"],diccionario["n"],diccionario["o"],diccionario["p"],diccionario["q"],diccionario["r"]],
        [diccionario["s"],diccionario["t"],diccionario["u"],diccionario["v"],diccionario["w"],diccionario["x"]],
        [diccionario["y"],diccionario["z"],diccionario["A"],diccionario["B"],diccionario["C"],diccionario["D"]],
        [diccionario["E"],diccionario["F"],diccionario["G"],diccionario["H"],diccionario["I"],diccionario["J"]]])
        print(m)

        #Sacando matriz inversa
        m1 = matrizinv(m)

        #Creando matriz de probabilidades
        p = probabilidad()

        #Generando multiplicación
        resultado = multi(m1,p)
        print()
        
        print(resultado)

        print()
        print()

        #Mostrando fraccionario
        frac(cantidadvar)

        print()

    else:
        print("El elemento está fuera de rango.")
        
    print()
    print()
