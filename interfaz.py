from colorama import *
from tabulate import tabulate
import nash_v2
import aversionalriesgov1
import estrategias_estrictamente_dominantes
import aversionalriesgolog

init(autoreset=True)

print(Style.BRIGHT+Fore.GREEN+"""              _____  _______  _    _  ______  ____   _____ __     __
             / ____||__   __|| |  | ||  ____|/ __ \ |  __ \\ \   / /
            | |  __    | |   | |__| || |__  | |  | || |__) |\ \_/ / 
            | | |_ |   | |   |  __  ||  __| | |  | ||  _  /  \   /  
            | |__| |   | |   | |  | || |____| |__| || | \ \   | |   
             \_____|   |_|   |_|  |_||______|\____/ |_|  \_\  |_|   
                                                                    """)
print()
print()
introduccion = " PER  ASPERA  AD  ASTRA "

print(Style.BRIGHT+Fore.YELLOW+introduccion.center(80, "="))

print()
print()

print(Style.BRIGHT+Fore.WHITE+"Bienvenido: ")

print()

while True:
    print()

    opciones = " Menú de Opciones "
    print(Style.BRIGHT+Fore.CYAN+opciones.center(80, "*"))

    lista = [[0, "Salir"],
    [1, "Aversión al Riesgo (Exponencial, Lineal, Radical) "],
    [2, "Aversión al Riego (Logaritmica) "],
    [3, "Estrategias Estrictamentes Dominantes"],
    [4, "Estrategia Mixta con Matrices Cuadradas (Gauss-Jordan-Nash)"]]
    
    print(Style.BRIGHT+Fore.GREEN+tabulate(lista))  
   
    print()
    print()
    
    a = int(input("Ingrese un número según el cálculo que desea realizar: "))

    if a==0:
        break
    elif a==1:
        aversionalriesgov1.main()
    elif a==2:
        aversionalriesgolog.main()
    elif a==3:
        estrategias_estrictamente_dominantes.main()
    elif a==4:
        nash_v2.main()

    print()
