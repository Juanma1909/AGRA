#G = [[1],[2],[3,4],[7],[5],[6,1],[2],[8],[3]]
import random
import networkx as nx
import matplotlib.pyplot as plt
"""las primeras 3 funciones, vease dfs, dfs_list,compute, hacen referencia a la
implementacion del algoritmo de kozaraju para sacar SCC, en este se invierte el grafo
se manda una dfs en el grafo invertido para poder obtener una lista, y por ultimo haciendo
uso de la lista mencionada anteriormente se manda una dfs tomando en cuenta los valores
de la lista.
En general la implementacion completa da como output un tupla, la cual contiene el numero de
SCC en el grafo y una lista donde a cada noso se le asigna el SCC al cual este pertenece"""
def dfs(u,num,G):
	global vis, scc
	vis[u] = 1
	scc[u] = int(num)
	for v in G[u]:
		if(vis[v] == 0):
			dfs(v,num,G)
	return

def dfs_list(u,G):
	global L, vis, I
	vis[u] = 1
	for v in I[u]:
		if(vis[v] == 0):
			dfs_list(v,G)
	L.append(u)
	return


def compute(G):
	global L,I, scc, vis
	n = len(G)
	scc = [-1 for i in range(n)]

	I = [[] for i in range(n)]
	for i in range(n):
		for j in G[i]:
			I[j].append(i)
	vis = [0 for i in range(n)]
	L = []
	for i in range(n):
		if(vis[i] == 0):
			dfs_list(i,G)
	vis = [0 for i in range(n)]
	cont = 0
	#print(L)
	while(len(L)):
		i = L.pop()
		if(vis[i] == 0):
			dfs(i,cont,G)
			cont +=	1	
	return (cont,scc)

def multStats(p_small,numV,qGraphs):
	"""mulStats es una funcion cuyo propposito es calcular los promedios de las metricas dadas
	segun ciertos parametros, dichos parametros son: p_small, el cual es un arreglo que contiene todos
	los p a los que se le va a calcular las metrica, numV el cual hace referencia al numero de vertices 
	a tomar en cuenta para la generacion de cada grafo, y qGraphs el cual indica cuantos grafos se van 
	generar por cada p perteneciente a p_small.

	se tienen 3 variables (avy1,avy2,avy3) en las cuales se va acumulando el valor de la 
	metrica correspondiente por cada grafo generado, al final de de qGraphs iteraciones  se halla 
	el promedio diviendo el acumulado por el numero de iteraciones, ese valor corresponde al p
	en el  que se este iterando en ese momento.

	la funcion tiene como output una tripleta que contiene 3 arreglos ( uno por cada metrica)
	cada uno de ellos contiene tantos elemtos, como p's contenga p_small."""
	joto = 0
	y1 = []
	y2 = []
	y3 = []
	for p in p_small:
		avy1=0
		avy2=0
		avy3=0
		for i in range(qGraphs):
			G,graph = erdos_renyi(numV,p)
			#G = []
			#for j in range(numV):
				#G1 = list(graph[j])
				#G.append(G1)
			m1 = compute(G)
			numscc = m1[0]
			scc = m1[1]	
			cPerScc= numV/numscc
			avy1 += numscc
			avy2 += cPerScc
			numEdges = 0
			for u in range(numV):
				for v in G[u]:
					if scc[u] != scc[v]:
						numEdges+=1
			avy3 += numEdges
			joto+=1
		avy1/=qGraphs
		avy2/=qGraphs
		avy3/=qGraphs
		y1.append(avy1)
		y2.append(avy2)
		y3.append(avy3)
	#print(joto)
	return(y1,y2,y3)
def punto1_2():
	"""En esta funcion se genera el p_small dado por la consigna del proyecto y se envia a la 
	funcion multStats, con numV = 100, y qGraphs = 500, para que genere en total 10000 grafos 
	aleatorios, luego simplemente se grafica haciendo uso de la biblioteca matplotlib

	NOTA:  para continuar con la ejecucion, debe cerrar la ventana de matplotlib"""
	print("1.2R/")
	p_small = [0.005*i for i in range(20)]
	s = multStats(p_small,100,500)
	y1,y2,y3 = s[0],s[1],s[2]
	plt.plot(p_small,y1, label = "Avrg Num of SCC")
	plt.plot(p_small,y2, label = "Avrg Size of SCC")
	plt.plot(p_small,y3, label = "Avrg Num of edges that connects 2 distinct SCC")
	plt.xlabel("P_Small")
	plt.ylabel("Average Values")
	plt.title("Random Graph Metrics")
	plt.legend()	
	plt.show()
	return
def punto1_1():
	print("1.1R/")
	"""esta funcion simplemente genera un grafo con 15 vertices y una probabilidad de 0.2 por 
	cada arco, haciendo uso de funciones anterirores, se consiguen las metricas necesarias y se
	imprimen

	NOTA:  para continuar con la ejecucion, debe cerrar la ventana de matplotlib"""
	n = 15
	p = 0.2
	seed = 42
	G,graph = erdos_renyi_seed(n,p,seed)	
	nx.draw(graph, with_labels = True)
	plt.show()
	# G = []
	# for i in range(n):
	# 	G1 = list(graph[i])
	# 	G.append(G1)
	m1 = compute(G)
	numscc = m1[0]
	scc = m1[1]	
	cPerScc= n/numscc
	print("numero de SCC´s: " + str(numscc))
	print("tamaño promedio de SCC´s: " + str(cPerScc))
	numEdges = 0
	for u in range(n):
		for v in G[u]:
			if scc[u] != scc[v]:
				numEdges+=1
	print("numero de edges que conectan 2 SCC´s distintos: " + str(numEdges))
	return


def erdos_renyi(n,p):
	G = [[] for _ in range(n)]
	E = []
	for i in range(n):
		for j in range(n):
			if i != j:
				dice = random.random()
				if dice <= p:
					G[i].append(j)
					E.append((i,j))
	G2 = nx.Graph()
	for i in range(n):
		G2.add_node(i)
	G2.add_edges_from(E)
	return (G,G2)

def erdos_renyi_seed(n,p,seed):
	random.seed(seed)
	G = [[] for _ in range(n)]
	E = []
	for i in range(n):
		for j in range(n):
			if i != j:
				dice = random.random()
				if dice <= p:
					G[i].append(j)
					E.append((i,j))
	G2 = nx.Graph()
	for i in range(n):
		G2.add_node(i)
	G2.add_edges_from(E)
	return (G,G2)
def calMax(p_small):
	"""esta funcion recibe un arreglo p_small y lo que hará sera calcular las metricas para cada p
	perteneciente a p_small, sabiendo que lo valores extremos de p_small nunca serán maximos 
	(p_small[0] y p_small[4]) se calcula el maximo, obteniendo su valor, si dicho valor el mayor que 
	maxVal(maximo hasta el momento) entonces se actualiza maxVal, se actualiza maxP y crea un nuevo
	rango procediendo de la misma froma que en la funcion punto1_3.
	note que si el valor maximo obtenido no es mayor al valor maximo hasta el momento, quiere decir que este
	es el mismo que el anterior (pues el valor maximo siempre se incluye en el nuevo arreglo), por tanto se
	consigue los valores inmediatamente anteriores posteriores a este en p_small y, por conveniecia, se halla
	la mita entre estos y el valor maximo, para asi crear un nuevo p_small que tambein contenga 5 valores """
	global maxVal,numG,maxP
	if numG < 8000:
		p_small2 = [p_small[1],p_small[3]]
		s = multStats(p_small2,100,100)
		y1,y2,y3 = s[0],s[1],s[2]
		#print(y3)
		pmax = max(y3)
		if pmax > maxVal:
			maxVal = pmax
			pmidix = y3.index(pmax)
			maxP = p_small[pmidix]
			lo,hi = p_small[pmidix-1],p_small[pmidix+1]
			mid = p_small[pmidix]
			mid0 = mid - 0.00001
			mid1 = mid + 0.00001
			newp = [lo,mid0,mid,mid1,hi]
			#print(newp)
			numG+=100*len(p_small)			
			#print(numG)
			return calMax(newp)
		else:
			lo = p_small[1]
			hi = p_small[3]
			newp=[lo,(lo+p_small[2])/2,p_small[2],(p_small[2]+hi)/2,hi]
			#print(newp)
			numG+=100*len(p_small)
			#print(numG)
			return calMax(newp)





def punto1_3():
	"""para calcular el maximo se va a subdividir el proceso en 2 partes, la pimera (esta) la cual
	hace lo siguiente: usando el mismo arreglo p_small proveido por el enunciado, se obtien las
	metricas para cada p, luego se buca el mayor valor obtenido y se obtiene su indice y su valor.
	con el indice lo que se hace es buscar en p_small los valores inmediatamente a la izquierda 
	derecha y los desnomina lo y hi respectivamente, luego busca el p correspondiente al maximo y
	le suma (y resta) 0.00001 para generear un nuevo rango con 5 probabilidades.

	esta funcion utiliza 3 globales, maxVal la cual almacena el valor maximo obtenido hasta el momento
	numG que almacena la cantidad de grafos que se han generado hasta el momento 
	(este será el cirterios de parada para hallar el maximo), y por ultimmo maxP el cual almacena el p
	correspondiente al valor maximo hallado"""
	global maxVal,numG,maxP
	print("1.3R/")
	maxVal = 0
	numG = 0
	maxP = 0
	p_small = [0.005*i for i in range(20)]
	s = multStats(p_small,100,200)
	y1,y2,y3 = s[0],s[1],s[2]
	pmax = max(y3)
	maxVal = pmax
	pmidix = y3.index(pmax)
	maxP = p_small[pmidix]
	lo,hi = p_small[pmidix-1],p_small[pmidix+1]
	mid = p_small[pmidix]
	mid0 = mid - 0.00001
	mid1 = mid + 0.00001
	newp = [lo,mid0,mid,mid1,hi]
	numG += 200*len(p_small)
	#print(numG)
	print("valor maximo inicial: " + str(pmax))
	calMax(newp)
	print("valor maximo optimizado: " + str(maxVal))
	print("p correspondiente al valor maximo:" + str(maxP))
	return





def main():			
	punto1_1()
	punto1_2()
	punto1_3()
	return
main()
