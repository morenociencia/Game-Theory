from math import *
import numpy as np 
import matplotlib.pyplot as plt 
from colorama import *

def main():
		
	init(autoreset=True)
	
	def space():
		
		espacio = "^"

		print(Style.BRIGHT+Fore.CYAN+espacio.center(80, "*"))

	print()
	
	print(Fore.GREEN+Style.BRIGHT+"BIENVENIDO A AVERSIÓN AL RIESGO")
	
	print()

	riquezainicial = float(input("Ingrese el valor de la riqueza inicial: "))
	
	print()
	print()

	print("Recuerde que entre mayor se la interpolación, la gráfica va a ser más exacta")
	print("Recomendación elija un valor entre 1 y 10")

	print()

	interpo = int(input("Ingrese la variabilidad de la interpolación: "))
	
	print()
	print()
	
	print("Ingrese el exponente de su función de Utilidad: ")
	f=bool(int(input("Ingrese 0 si es un FRACCIONARIO, de lo contrario escriba 1: ")))

	print()
	print()

	if f==True:
		var3=float(input("Ingrese el valor de tetta (exponente entero): "))
	else:
		tettanum=int(input("Ingrese el numerador de tetta: "))
		tettadenom=int(input("Ingrese el denominador de tetta: "))
		var3=(tettanum)/tettadenom

	print()
	print()

	space()

	print()
	print()

	print(Fore.GREEN+Style.BRIGHT+"Recuerde que alfa 1 es la probabilidad correspondiente a x1")
	
	alfa = float(input("Ingrese el valor de la probabilidad alfa 1: "))
	x1 = float(input("Ingrese el valor de x1: "))
	x2 = float(input("Ingrese el valor de x2: "))
	
	betta = (1-alfa)
	
	print()
	
	print(Fore.GREEN+"El valor de su alfa 2, correspondiente a x2 es: ", betta) 

	print()
	print()

	space()

	#Calculando los puntos especificos
	x = (alfa*x1)+(betta*x2)
	
	print()
	
	print(Fore.YELLOW+"Su valor de x en el punto de probabilidad indicada es: ", x)
	
	y = (alfa*(x1**var3))+(betta*(x2**var3))
	
	print()
	
	print(Fore.YELLOW+"Su valor de y en el punto de probabilidad indicada es: ", y)
	
	print()
	print()

	space()

	#Se crea condicional if para usar el valor ingresado que sea mayor

	if x1>x2:
		var0 = x1
	elif x1<x2:
		var0 = x2
	else:
		print("Los valores introducidos en x1 e x2 no pueden ser calculados")

	print(type(var0))
	input()
	#Creando variable importante
	cantidadinterpo = int(var0)*interpo
	#print()
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	#print(var0)
	#--------------------------------------------Valores x
	#se usa lindspace para la interpolación
	valoresx = np.linspace(0, int(var0), num=cantidadinterpo) #, num=(var0*2))
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	print(type(valoresx))
	print(Fore.RED+"Valores de x para la interpolación unitaria ", valoresx)
	input()
	#print()
	#-------------------------------------------Valores y
	#Se crea una lista vacía que va a almacenar los resultados de la Utilidad
	valoresy = []
	for i in range(cantidadinterpo):
		valoresy.append((valoresx[i])**(var3))
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	#print(Fore.GREEN+"Lista de resultados de los valores x evaluados en la función y ", valoresy[:])
	#print()
	arraysy = np.array(valoresy)
	print(type(arraysy))
	print(Fore.GREEN+"Lista de resultados de los valores x evaluados en la función y ", arraysy)
	print()
	input()
	#Generando gráfica de Utilidad Esperada
	#---------------------------------------Lista de Probabilidad
	p = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
	#Se crea bucle for
	valoresx1 = []
	for i in p:
		valoresx1.append((x1*i)+((1-i)*x2))
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	print(Fore.YELLOW+"Valores de x según la probabilidad ",valoresx1[:])
	print()
	input()
	#Es necesario crear un condicional, y duplicar valor debido a que la interpolación es de 2

	var1 = int(x1*interpo)-1
	var2 = int(x2*interpo)-1
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	#print(len(valoresy))
	#print(valoresy[var1])
	#print(valoresy[var2])
	#input()


	#Se crea lista vacia que almacene los valores de y es decir ue
	valoresy1 = []
	for i in p:
		valoresy1.append((i*(valoresy[var1]))+((1-i)*(valoresy[var2])))
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	print(Fore.CYAN+"Valores de y evaluados según los x de probabilidad ", valoresy1[:])
	print()
	input()

	#Convirtiendo a arrays ciertas listas para evitar errores matemáticos y lograr una carga más rapida.
	#arraysx = np.array(valoresx)
	arraysx1 = np.array(valoresx1)
	arraysy1 = np.array(valoresy1)
	#Buscando Pendiente de la función de utilidad esperada
	if x1>x2:
		m= ((arraysy1[10])-(arraysy1[0]))/(x1-x2)
	elif x2>x1:
		m= ((arraysy1[0])-(arraysy1[10]))/(x2-x1)
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	#print(arraysy1[10])
	#print(arraysy1[0])
	#print(m)
	#print()
	#Encontrando Valor de la constante de su función de utilidad esperada, b de y=mx+b
	#La constante va a ser llamada k
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	#print(arraysy1[10])
	#print()
	k = (arraysy1[10])-(m*x1)
	#print(k)
	print()
	print()
	#Hallando prima de riesgo
	if f==True:
		bx = y**(1/(var3)) #todavia no se ha definido proceso matematico
	else:
		bx = y**(tettadenom)
	print()
	print("Aquí está Wec: ", bx)
	print("Aquí está el otro: ", x)
	print()
	pr = x-(bx)
	print(Fore.CYAN+"Su prima de riesgo es: ", pr)
	print()
	#Mirando si puede pagar riesgo con riqueza inicial
	prri = riquezainicial-pr
	if prri>=0:
		print(Fore.GREEN+"El sujeto Si puede pagar el riesgo")
	elif prri<0:
		print(Fore.RED+"El sujeto NO puede pagar el riesgo")
	#Hallando integral de la utilidad

	#mostrando prima de riesgo
	#fprx = np.arange(0, 11)
	#fpry = 20

	#Graficando puntos regerentes a la prima de riesgo.
	plt.plot(bx,y, marker="o", color="red")
	plt.plot(x,y, marker="o", color="red")
	plt.hlines(y=y, xmin=bx, xmax=x, label="Prima de Riesgo", color="red")
	#plt.plot(fprx, fpry, "ob")
	plt.plot(valoresx, arraysy, label="Utilidad")
	plt.plot(arraysx1, arraysy1, label="Utilidad Esperada")

	plt.grid()
	plt.legend()
	plt.xlabel("W (Riqueza)")
	plt.ylabel("U (Utilidad)")
	plt.title("Elección Bajo Incertidumbre")

	plt.show()

	input()

if __name__=="__main__":
	main()