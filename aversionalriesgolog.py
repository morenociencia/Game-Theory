from math import *
import numpy as np 
import matplotlib.pyplot as plt 
from colorama import *

def main():

	init()
	print(Fore.WHITE+Style.BRIGHT+""" 
	___  ___ ___  _ __   ___  _ __ ___  ___ 
	/ _ \/ __/ _ \| '_ \ / _ \| '_ ` _ \/ __|
	|  __/ (_| (_) | | | | (_) | | | | | \__ \

	\___|\___\___/|_| |_|\___/|_| |_| |_|___/
											""")

	riquezainicial = float(input("Ingrese el valor de la riqueza inicial: "))
	print()
	print()
	print(Fore.CYAN+"********************************************************************************")
	print()
	print()
	print(Fore.GREEN+Style.BRIGHT+"Recuerde que alfa 1 es la probabilidad correspondiente a x1")
	print(Fore.WHITE)
	alfa = float(input("Ingrese el valor de la probabilidad alfa 1: "))
	x1 = float(input("Ingrese el valor de x1: "))
	x2 = float(input("Ingrese el valor de x2: "))
	betta = (1-alfa)
	print()
	print(Fore.GREEN+"El valor de su alfa 2, correspondiente a x2 es: ", betta) 
	print()
	print()
	print("********************************************************************************")
	#Calculando los puntos especificos
	x = (alfa*x1)+(betta*x2)
	print()
	print(Fore.YELLOW)
	print("Su valor de x en el punto de probabilidad indicada es: ", x)
	y = (alfa*(log(x1)))+(betta*(log(x2)))
	print()
	print("Su valor de y en el punto de probabilidad indicada es: ", y)
	print()
	print()
	print("********************************************************************************")
	#Se crea lista vacia que almacena valores básicos de interpolación
	valoresx = []
	#Se crea condicional if para usar el valor ingresado que sea mayor

	if x1>x2:
		var0 = x1+1
	elif x1<x2:
		var0 = x2+1
	else:
		print("Los valores introducidos en x1 e x2 no pueden ser calculados")

	#print()
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	#print(var0)
	#--------------------------------------------Valores x
	#Se crea el bucle for
	for i in range(1, int(var0)):
		valoresx.append(i)
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	print(Fore.RED+"Valores de x para la interpolación unitaria ", valoresx[:])
	#print()
	#-------------------------------------------Valores y
	#Se crea lista Vacía que va a almacenar los resultados de la Utilidad
	valoresy = []
	for i in range(1, int(var0)):
		valoresy.append(log(i))
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	print(Fore.GREEN+"Lista de resultados de los valores x evaluados en la función y ", valoresy[:])
	print()
	#Generando gráfica de Utilidad Esperada
	#---------------------------------------Lista de Probabilidad
	p = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
	#Se crea bucle for
	valoresx1 = []
	for i in p:
		valoresx1.append((x1*i)+((1-i)*x2))
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	print(Fore.YELLOW+"Valores de x según la probabilidad ",valoresx1[:])
	#print()
	#Se crean variables especiales para el bucle for
	valorespecial1 = x1-1
	valorespecial2 = x2-1
	#Se crea lista vacia que almacene los valores de y es decir ue
	valoresy1 = []
	for i in p:
		valoresy1.append((i*(valoresy[int(valorespecial1)]))+((1-i)*(valoresy[int(valorespecial2)])))
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	print(Fore.CYAN+"Valores de y evaluados según los x de probabilidad ", valoresy1[:])
	#print()
	#Convirtiendo a arrays ciertas listas para evitar errores matemáticos y lograr una carga más rapida.
	arraysx = np.array(valoresx)
	arraysy = np.array(valoresy)
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
	bx = e**(y)
	#///////////PUNTO DE CONTROL\\\\\\\\\\
	#print(bx)
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
	plt.plot(arraysx, arraysy, label="Utilidad")
	plt.plot(arraysx1, arraysy1, label="Utilidad Esperada")

	plt.grid()
	plt.legend()
	plt.xlabel("W (Riqueza)")
	plt.ylabel("U (Utilidad)")
	plt.title("Elección Bajo Incertidumbre")

	plt.show()

	input()

if __name__ == "__main__":
	main()