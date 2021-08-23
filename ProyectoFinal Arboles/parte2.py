
import random
import networkx as nx
import matplotlib.pyplot as plt
def getTrip(x):
	"""getTrip es una funcion que permite obtener todas las permitacions de una tripleta, esta son añadidas
	a una lista y las retorna"""
	a,b,c=x[0],x[1],x[2]
	t2=(a,c,b)
	t3=(b,a,c)
	t4=(b,c,a)
	t5=(c,a,b)
	t6=(c,b,a)
	return[t2,t3,t4,t5,t6]

def deg(G):
	"""deg es una funcion que permite calcular el grado por nodo perteneciente al grafo G
	esto lo hace haciendo uso de la longitud de la lista de adyacencia de cada nodo
	pues es la longitud de esta la que indica el numero de conexiones desde y hasta dicho nodo.
	este degree se va acumulando y luego se saca el promedio de este, para finalmente retornarlo"""
	n = len(G)
	avnDeg = 0
	for u in range(n):
		degree = len(G[u])
		#print(degree)
		avnDeg +=degree
	avnDeg/=n
	return avnDeg

def tripTrian(G):
	"""esta funcion recibe un garfo G y retorna la cantidad de triangulos y de tripletas 
	que este tiene, para calcular dichso valores se hace uso de un triple for anidado el cual
	itera sobre las listas de adyacencia, al encontrar una tripleta debe preguntar si todos los 
	nodos de dicha tripleta son diferentes (pues al ser G no dirigidos puede volver a un nodo ya visitado)
	luego hace uso de la funcion getTrip la cual retorna todas las permutaciones de una tripleta
	estas permutaciones las guarda en un set de tal manera que no se vuelvan a repetir en caso de encontrar 
	la misma tripleta solo que en una de sus posibles permutaciones.

	para trianglulos simplemente se agrega el condicional de si u pertenece a la lista de adyacencia de w
	de ser asi se procede de manera smejante que con una tripleta normal"""
	n = len(G)
	trip = set()
	trian = set()
	for u in range(n):
		for v in G[u]:
			for w in G[v]:
				if v !=u and v!=w and u != w:
					trip.add((u,v,w))
					s = getTrip((u,v,w))
					if u in G[w]:
						trip.add((u,v,w))
						trian.update(s)
						trip.update(s)
					else:
						trip.update(s)

	return (len(trian)/6,len(trip)/6)

def dfs(G,u,parent,ap,depth,low,bridges):
	"""esta funcion los que hace es crear un arbol de dfs donde depth es la profundidad del nodo
	y low es que tan arrbiab puede llegar un nodo bajamdo todo lo que pueda y subiendo solo
	una vez (mediante un back edge).
	se procede de forma igual que un tarjan, lo unico que vcambia es a la hora de llegar a un back edge,
	pues al ser G un grafo no dirigido siempre habria un back edge hacia el padre de v, para 
	eviatr esto se ponel el condicional de que en caso de encontrar un back edge, v no puede ser 
	el padre de u.
	"""
	children = 0
	for v in G[u]:
		if depth[v] ==-1:
			depth[v] = low[v] = depth[u]+1
			parent[v] = u
			children+=1
			dfs(G,v,parent,ap,depth,low,bridges)
			low[u] = min(low[u],low[v])
			if parent[u] == -1 and children > 1:
				ap[u] = 1
			if parent[u] != -1 and low[v] >= depth[u]:
				ap[u] = 1
			if low[v] > depth[u]:
				bridges.append((u,v))
		elif depth[v] < depth[u] and parent[u]!=v:
			low[u] = min(low[u],depth[v])
	return

def tarjan(G):
	"""esta funcion recibe un grafo G, crea un arreglo de padres, de puntos de articulacion, de
	profundidad, de low y de bridges para que al llamar a la dfs se puedan hallar los puntos de articulacion y los puentes
	una vez teniendo el arreglo con los puntos de articulacion se itera sobre este y se obtiene el numero de puntos de
	articulacion que hay en el grafo, sacando la longitud del arreglo de puentes se obtine el valor de numero de punetes en 
	el grafo G."""
	n = len(G)
	parent = [-1 for _ in range(n)]
	ap=[0 for _ in range(n)]
	depth = [-1 for _ in range(n)]
	low = [-1 for _ in range(n)]
	bridges = []
	for u in range(n):
		if depth[u]==-1:
			depth[u]=low[u]=0
			dfs(G,u,parent,ap,depth,low,bridges)

	cap = 0
	for i in range(n):
		if ap[i] == 1:
			cap+=1
	return (cap,len(bridges))

def dfsCC(G,vis,u):
	""" esta funcion recibe un garfo G un arreglo de visitados y un vertice u a partir del cual se
	inicia la dfs.
	Es una dfs que va iterando a partir de una lista de adyacencia de un u original,
	cuando ya no hay mas vertices por visitar en las listas de adyacencia vuelve afuera de la funcion,
	indicando que se ha terminado un componente conexo."""
	vis[u] = True
	for v in G[u]:
		if vis[v] == False:
			dfsCC(G,vis,v)
	return

def multStats3(p_large,numV,qGraphs):
	"""esta funcion recibe un arreglo de p´s llamado p_large, el numero de vertices pomr grafo y el numero
	de grafos a generar por cada p perteneciente a p_large.
	para calcular el numero de triangulos y triplewtas se hace un llamdo a la funcion tripTrian la cual
	recibe un grafo G y retorna el numero de tripletas y triangulos en G.

	se tienen 3 variables (avy2,avy3,avy4) en las cuales se va acumulando el valor de la 
	metrica correspondiente por cada grafo generado, al final de de qGraphs iteraciones  se halla 
	el promedio diviendo el acumulado por el numero de iteraciones, ese valor corresponde al p
	en el  que se este iterando en ese momento.

	la funcion tiene como output una tripleta que contiene 3 arreglos ( uno por cada metrica)
	cada uno de ellos contiene tantos elemtos, como p's contenga p_large."""
	y2,y3,y4 = [],[],[]
	joto = 0
	for p in p_large:
		avy2,avy3,avy4 = 0,0,0
		for i in range(qGraphs):
			G,graph = erdos_renyi(numV,p)
			vis = [False for _ in range(numV)]			
			t = tripTrian(G)
			numTrian,numTrip = t[0],t[1]
			avy2+=numTrian
			avy3+=numTrip
			if numTrip != 0:
				avy4+=numTrian/numTrip
			joto+=1
		avy2/=qGraphs
		avy3/=qGraphs
		avy4/=qGraphs
		y2.append(avy2)
		y3.append(avy3)
		y4.append(avy4)

	return(y2,y3,y4)





def multStats2(p_small,numV,qGraphs):
	"""esta funcion recibe un arreglo de p´s llamado p_small, el numero de vertices pomr grafo y el numero
	de grafos a generar por cada p perteneciente a p_small.
	para calcular el numero de puntos de articulacion y ellnumero de punetes el grafo, se hace uso del 
	algoritmo de tarjan, posteriormente se calcula ell numero de CC para asi poder obtener el tamaño
	promedio por CC.

	se tienen 5 variables (avy1,avy2,avy3,avy4,avy5) en las cuales se va acumulando el valor de la 
	metrica correspondiente por cada grafo generado, al final de de qGraphs iteraciones  se halla 
	el promedio diviendo el acumulado por el numero de iteraciones, ese valor corresponde al p
	en el  que se este iterando en ese momento.

	la funcion tiene como output una tripleta que contiene 5 arreglos ( uno por cada metrica)
	cada uno de ellos contiene tantos elemtos, como p's contenga p_small."""
	y1,y2,y3,y4,y5 = [],[],[],[],[]
	joto = 0
	for p in p_small:
		avy1,avy2,avy3,avy4,avy5 = 0,0,0,0,0
		for i in range(qGraphs):
			G,graph = erdos_renyi(numV,p)
			vis = [False for _ in range(numV)]			
			m1 = tarjan(G)
			numCC = 0
			for u in range(numV):
				if vis[u] == False:
					numCC+=1
					dfsCC(G,vis,u)
			avNumCC = numV/numCC
			numAp,numB = m1[0],m1[1]
			avnDeg = deg(G)
			avy1+=numAp
			avy2+=numB
			avy3+=avNumCC
			avy4+=avnDeg
			avy5+=numCC
			joto+=1
		avy1/=qGraphs
		avy2/=qGraphs
		avy3/=qGraphs
		avy4/=qGraphs
		avy5/=qGraphs
		y1.append(avy1)
		y2.append(avy2)
		y3.append(avy3)
		y4.append(avy4)
		y5.append(avy5)
	#print(joto)
	return (y1,y2,y3,y4,y5)

def multStats4(p_large,numV,qGraphs):
	"""esta funcion recibe un arreglo de p´s llamado p_large, el numero de vertices y el numero de
	grafos a generar por cada p perteneciente a p_large, con cada grafo hace uso de una dfs que cuenta el
	numero de componentes conexos, pues cada vez que sale de la recursion de dfsCC significa que acabó 
	todo un componente conexo"""
	y1 = []
	joto = 0
	for p in p_large:
		avy1 = 0
		for i in range(qGraphs):
			G,graph = erdos_renyi(numV,p)
			vis = [False for _ in range(numV)]			
			numCC = 0
			for u in range(numV):
				if vis[u] == False:
					numCC+=1
					dfsCC(G,vis,u)
			avy1+= numCC
		avy1/=qGraphs
		y1.append(avy1)
	return y1


def punto2_1():
	"""esta funcion simplemente genera un grafo erdos-renyi no dirigido con 15 vertices y una probabilidad de 0.2 por 
	cada arco, haciendo uso de funciones anterirores, se consiguen las metricas necesarias y se
	imprimen

	NOTA:  para continuar con la ejecucion, debe cerrar la ventana de matplotlib"""
	print("2.1R/")
	n = 15
	p = 0.2
	seed = 12
	vis = [False for i in range(n)]
	G,graph=erdos_renyi_seed(n,p,seed)
	nx.draw(graph,with_labels = True)
	plt.show()	
	m1 = tarjan(G)
	numCC = 0
	for u in range(n):
		if vis[u] == False:
			numCC+=1
			dfsCC(G,vis,u)

	avNumCC = n/numCC
	numAp,numB = m1[0],m1[1]
	avnDeg = deg(G)
	t = tripTrian(G)
	numTrian,numTrip = t[0],t[1]
	print("numero de componentes conectados: " + str(numCC))
	print("tamaño promedio de componentes conectados: " + str(avNumCC))
	print("numero de puntos de articulacion: " + str(numAp))
	print("numero de puentes: " + str(numB))
	print("Grado promedio por nodo: " + str(avnDeg))
	print("numero de triangulos: " + str(numTrian))
	print("numero de tripletas: " + str(numTrip))
	return

def punto2_2():
	"""En esta funcion se genera el p_small, un p_large y la union de estos, se envia a la 
	funcion multStats2, con numV = 100, y qGraphs = 500, para que genere en total 10000 grafos 
	aleatorios, luego simplemente se grafica haciendo uso de la biblioteca matplotlib la primera de las grafica.
	para la segunda se procede de manera similar solo que esta vez se hace un llamado a mulstats3 y a multstats4
	con p_small unido a p_large, posteriormente se grafican los valores haciendo uso de la libreria matplotlib

	NOTA:  para continuar con la ejecucion, debe cerrar la ventana de matplotlib"""
	print("2.2R/")
	p_small = [0.005*i for i in range(20)]
	p_large =[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]
	p_large=  p_small + p_large	
	s = multStats2(p_small,100,500)
	y1,y2,y3,y4,y5= s[0],s[1],s[2],s[3],s[4]
	plt.plot(p_small,y1, label = "Avrg num of ArtP")
	plt.plot(p_small,y2, label = "Avrg num of Brid")
	plt.plot(p_small,y3, label = "Avrg size per CC")
	plt.plot(p_small,y4, label = "Avrg node Deg")
	#plt.plot(p_small,y5)
	plt.xlabel("P_Small")
	plt.ylabel("Average Values")
	plt.title("Random Graph Metrics")
	plt.legend()
	plt.show()
	s = multStats3(p_large,20,100)
	y2,y3,y4 = s[0],s[1],s[2]
	y1 = multStats4(p_large,100,500)
	plt.plot(p_large,y1, label = "Avrg num of CC")
	plt.plot(p_large,y2, label = "Avrg num of triangles")
	plt.plot(p_large,y3, label = "Avrg num of triplets")
	plt.plot(p_large,y4, label = "#triangles/#triplets")
	plt.xlabel("P_Small & P_Large")
	plt.ylabel("Average Values")
	plt.title("Random Graph Metrics")
	plt.legend()
	plt.show()
	return


def calMax(p_small,x):
	"""esta funcion recibe un arreglo p_small y un x, este ultimo lo que hace es decidir que grafica 
	optimizar, lo que hará sera calcular las metricas para cada p al cual no se le haya sacado el valor antes
	es decir, para p_small[1] y p_small[3], poteriormente se calcula el maximo, obteniendo su valor, si dicho
	 valor el mayor que maxVal(maximo hasta el momento) entonces se actualiza maxVal, se actualiza maxP y crea un nuevo
	rango procediendo de la misma froma que en la funcion punto1_3.
	note que si el valor maximo obtenido no es mayor al valor maximo hasta el momento, quiere decir que este
	es el mismo que el anterior (pues el valor maximo siempre se incluye en el nuevo arreglo), por tanto se
	consigue los valores inmediatamente anteriores posteriores a este en p_small y, por conveniecia, se halla
	la mita entre estos y el valor maximo, para asi crear un nuevo p_small que tambein contenga 5 valores"""
	global maxVal,numG,maxP	
	if numG < 8000:
		p_small2 = [p_small[1],p_small[3]]
		s = multStats2(p_small2,100,100)
		maxy = s[x]		
		maxAp = max(maxy)
		if maxAp > maxVal:
			maxVal = maxAp
			aPMidx = maxy.index(maxAp)			
			maxP = p_small[aPMidx]
			lo,hi = p_small[aPMidx-1],p_small[aPMidx+1]
			mid = p_small[aPMidx]
			mid0,mid1 = mid - 0.00001, mid + 0.00001
			newp = [lo,mid0,p_small[aPMidx],mid1,hi]
			numG+=100*len(p_small2)
			return calMax(newp,x)
		else:
			lo = p_small[1]
			hi = p_small[3]
			newp=[lo,(lo+p_small[2])/2,p_small[2],(p_small[2]+hi)/2,hi]
			numG+=100*len(p_small2)
			return calMax(newp,x)
def punto2_3():
	"""para calcular el maximo se va a subdividir el proceso en 2 partes, la pimera (esta) la cual
	hace lo siguiente: usando los mismos arreglos p_small y p_large (y la union de estos) proveidos por el enunciado, se obtien las
	metricas para cada p, luego se buca el mayor valor obtenido y se obtiene su indice y su valor.
	con el indice lo que se hace es buscar en p_small los valores inmediatamente a la izquierda 
	derecha y los desnomina lo y hi respectivamente, luego busca el p correspondiente al maximo y
	le suma (y resta) 0.00001 para generear un nuevo rango con 5 probabilidades. El procedimiento especificado
	anterior mente lo hace en 2 ocaciones pues se pide calcular el maximo tanto para el numero de puntos de articulacion
	como para bridges

	esta funcion utiliza 3 globales, maxVal la cual almacena el valor maximo obtenido hasta el momento
	numG que almacena la cantidad de grafos que se han generado hasta el momento 
	(este será el cirterios de parada para hallar el maximo), y por ultimmo maxP el cual almacena el p
	correspondiente al valor maximo hallado"""
	global maxVal,numG,maxP
	print("2.3R/")
	maxVal,numG,maxP = 0,0,0
	p_small = [0.005*i for i in range(20)]
	s = multStats2(p_small,100,200)
	y1,y2 = s[0],s[1]
	maxAp = max(y1)
	maxVal = maxAp
	aPMidx = y1.index(maxAp)
	maxP = p_small[aPMidx]
	lo,hi = p_small[aPMidx-1],p_small[aPMidx+1]
	mid = p_small[aPMidx]
	mid0,mid1 = mid - 0.00001, mid + 0.00001
	newp = [lo,mid0,p_small[aPMidx],mid1,hi]
	numG+=200*len(p_small)
	print("Valor maximo inicial para ArtP:" + str(maxAp))
	calMax(newp,0)
	print("valor maximo optimizado para ArtP: " + str(maxVal))
	print("p correspondiente al valor maximo para ArtP:" + str(maxP))
	maxVal,numG,maxP = 0,0,0
	maxBr = max(y2)
	maxVal = maxBr
	brMidx = y2.index(maxBr)
	maxP = p_small[brMidx]
	lo,hi = p_small[brMidx-1],p_small[brMidx+1]
	mid = p_small[brMidx]
	mid0,mid1 = mid - 0.00001 , mid + 0.00001
	newp = [lo,mid0,p_small[brMidx],mid1,hi]
	numG+=200*len(p_small)
	print("Valor maximo inicial para Brid:" + str(maxBr))
	calMax(newp,1)
	print("valor maximo optimizado para Brid: " + str(maxVal))
	print("p correspondiente al valor maximo para Brid:" + str(maxP))
	return

def erdos_renyi(n,p):
	"""funciona de manera igual a la anterior unicamente que no posee ninguna seed, por tanto
	al llamarla se obtinen resultados aleatorios"""
	assert n>= 0 and 0 <= p <=1
	G = [[] for _ in range(n)]
	E = []
	for u in range(n):
		for v in range(u+1,n):
			q = random.random()
			if q < p:
				E.append((u,v))
				G[u].append(v)
				G[v].append(u)

	G2 = nx.Graph()
	for i in range(n):
		G2.add_node(i)

	G2.add_edges_from(E)

	return (G,G2)

def erdos_renyi_seed(n,p,seed):
	"""Este es la funcion que genera los grafos no dirigidos de tipi erdos-renyi, existen 2 variantes de la misma funcion:
	la primera sería esta la cual recibe ademas de un N y un P, una seed, para que los resultados obtenidos por esta funcion
	sean repetibles, esta va iterando sobre los nodos y pregunta si existe un arco entre ellos, de ser asi
	lo añade a una lista de arcos la cual es utilizada para crear el grafo de networkx y poderlo
	graficar"""
	random.seed(seed)
	assert n>= 0 and 0 <= p <=1
	G = [[] for _ in range(n)]
	E = []
	for u in range(n):
		for v in range(u+1,n):
			q = random.random()
			if q < p:
				E.append((u,v))
				G[u].append(v)
				G[v].append(u)

	G2 = nx.Graph()
	for i in range(n):
		G2.add_node(i)

	G2.add_edges_from(E)

	return (G,G2)



def main():
	punto2_1()
	punto2_2()
	punto2_3()
	return
main()
