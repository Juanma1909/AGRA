import numpy as np
import matplotlib.pyplot as plt
from operator import attrgetter
import math
import random
INF = float('inf')
time = 0
# def exponencial(p):
# 	exp = random.random()
# 	prob = -p*math.log(1-exp)
# 	return prob
def createTime():
	"""se crea un tiempo tomando como base el tiempo del ultimo bloque creado y un distribucion 
	exponencial """
	global time
	newTime = time +np.random.exponential(1.0)
	#newTime = time + exponencial(1.0)
	time = newTime
	#print(time)
	return newTime
def createDelay(p):
	"""se crea un delay con distribucion exponencial"""
	delay = np.random.exponential(p)
	#delay = exponencial(p)
	return delay
class Block:
	"""La clase bloque hace referencia a los bloque que conforman una blockchain, en este se 
	alamcen 4 atributos: timeB, que es el timepo en el que el bloque fue decubierto, depthB,
	el cual es la profundidad en la que se encuentra el bloque, numB que proporciona informacion
	acerca de qué bloque es (numero, identificador) y por ultimo parentB, el cual es qué bloque es padre
	del este bloque.

	esta clase posee 2 metodos: su constructor el cual inicializa por defecto tanto el padre como la
	profundidad(pues estos serán calculados posteriormente a su creacion), y recibe 2 parametros los cuales son,
	el tiempo en el que fue descubierto el bloque y el numero o identificador de bloque. el segundo metodo
	cumple la funcion de visualizar en pantalla todos los atributos del bloque en el que se esté en este momento"""
	def __init__(self,t,num):
		self.timeB = t
		self.depthB = 0
		self.numB = num
		self.parentB = None
		return
	def showStats(self):
		print(self.timeB)
		print(self.depthB)
		print(self.numB)
		return
class Chain:
	"""Chain es una clase que hace referencia al arbol de blockchain, esta posee unicamente 1 atributo
	el cual es una lista, llamada tree, la cual está compuesta por objetos de tipo bloque, al cada bloque tener conocimiento
	de su padre, de manera general es una lista de padres.
	
	esta clase posee 3 metodos, el primero es el constructor que unicamente crea el arreglo tree, y lo inicializa
	con el bloque padre, es decir, aque que tiene profundidad 0, identificador 0, tiempo 0 y sin padre. el segundo lo que hace es añadir 
	un bloque al blockchain, para ello hace uso de el exponential random, para generar tanto el timepo como el delay (el timepo depende del timepo del bloque anterior)
	posteriormente se buscan aquellos bloques de los que se tiene conocimiento, una vez se tiene dicho conjunto,
	se busca cual tiene la profundidad mas grande(la rama más larga) y se escoge aquel que tenga dicha profundidad y el menor tiempo de descubrimiento
	finalmente se actualizan tanto la profundidad como el padre de aquel bloque que se quiere añadir al blockchain y se añade al arreglo tree.

	el ultimo metodo hace uso del atributo padre para contar cuantos bloques existen en la rama más larga, de tal manera que se itera hasta
	que el padre sea none ( es decir la raiz)"""
	def __init__(self):
		a = Block(0,0)
		self.tree =[a]
		return
	def add(self,p,num):		
		d = createDelay(p)
		t = createTime()
		b = Block(t,num)
		visual = b.timeB - d		
		i = 1
		stop = False

		while i < len(self.tree) and stop!=True:
			if self.tree[i].timeB > visual:
				stop=True
				i-=1
			i+=1

		see = self.tree[:i]
		maximo = max(see, key=attrgetter('depthB'))
		maximo = maximo.depthB		
		minTime = INF
		minBlock = 0

		for j in range(len(see)):
			jblock = see[j]			
			if jblock.depthB == maximo:
				if jblock.timeB < minTime:					
					minTime =jblock.timeB
					minBlock = j		
		b.depthB = see[minBlock].depthB + 1
		b.parentB = see[minBlock]
		self.tree.append(b)
		return

	def largestBranch(self):
		largest = max(self.tree, key = attrgetter('depthB'))
		nump = 1
		while largest.parentB != None:
			largest = largest.parentB
			nump+=1
		return nump
def multstats(pgrad,n,it):
	"""mulStats es una funcion cuyo propposito es calcular los promedios de las metricas dadas
	segun ciertos parametros, dichos parametros son:pgrad, el cual es un arreglo que contiene todos los p,
	n el cual hace referencia la numero de bloques a generar por cada blockchain generado, e it que indica
	cuantos blockchain se generarán por cada p en la lista de pgrad.

	se tienen 2 variables (avy1,avy2) en las cuales se va acumulando el valor de la 
	metrica correspondiente por cada blockchain generado, al final de de it iteraciones  se halla 
	el promedio diviendo el acumulado por el numero de iteraciones, ese valor corresponde al p
	en el  que se este iterando en ese momento.

	la funcion tiene como output una tupla que contiene 2 arreglos ( uno por cada metrica)
	cada uno de ellos contiene tantos elemtos, como p's contenga pgrad.	"""
	global time 
	y1,y2 = [],[]
	for p in pgrad:
		avy1,avy2 = 0,0
		for i in range(it):
			time = 0
			cantBlocks = 1
			bChain = Chain()
			for i in range(n):
				bChain.add(p,cantBlocks)
				cantBlocks+=1
			lB = bChain.largestBranch()
			bP = n+1 - lB
			avy1+=lB
			avy2+=bP
		avy1/=it
		avy2/=it
		y1.append(avy1)
		y2.append(avy2)				
	return (y1,y2)

def punto3_1():
	"""En esta funcion se genera el pgrad dado por la consigna del proyecto y se envia a la 
	funcion multStats, con n = 1000, e it = 200, para que genere en total  8000 blockchain 
	aleatorios, luego simplemente se grafica haciendo uso de la biblioteca matplotlib

	NOTA:  para continuar con la ejecucion, debe cerrar la ventana de matplotlib"""
	print("3.1R/")
	pgrad = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35,
	0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85,
	0.9, 0.95, 1.0, 1.05, 1.1, 1.15,  1.2, 1.25, 1.3, 1.35,
	1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85,
	1.9, 1.95, 2.0]
	n = 999
	it = 200
	s = multstats(pgrad,n,it)
	y1,y2 = s[0],s[1]
	plt.plot(pgrad,y1, label = "Avrg size of largestBr")
	plt.plot(pgrad,y2, label = "Avrg num of lost blocks")
	plt.xlabel("P_Grad")
	plt.ylabel("Average Values")
	plt.title("Block Chain Metrics")
	plt.legend()
	plt.show()
	return


def main():
	punto3_1()
	return
main()
"""3.2.1 a medida que el p tiende a infinito el numero de bloques perdidos tiende a aumentar pues el delay tiende a ser mayor, haciendo 
los bloques no tengan tanta visibilidad de los que ya estan el el blockchain, por ende la curva de bloques perdidos tiende a 1000 (para mil bloques)
y la curva de rama mas larga tiende a 1, pues todos los bloques tenderían a quedar pegados al bloque padre (el bloque 0)"""
"""3.2.2"""




