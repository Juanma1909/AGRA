from sys import stdin
def hakaiSort(G,aux):
	n = len(G)
	indeg=[0 for i in range(n)]
	for u in range(n):
		for v in G[u]:
			#hay un arco u-->v
			pos = aux.index(v)
			indeg[pos]+=1
	topo=[]
	while len(topo)<n:
		for i in range(n):
			if indeg[i]==0:
				topo.append(aux[i])
				for j in G[i]:
					pos = aux.index(j)
					indeg[pos]-=1
				indeg[i]=-1
	print("".join(topo))
	return topo

def solve(dicc):
	aux = []
	graph = []
	tam = len(dicc)
	for i in range(tam - 1):
		cm1 = dicc[i]
		cm2 = dicc[i+1]
		diff = False
		j = 0 
		while j < min(len(cm1),len(cm2)) and diff == False :
			if cm1[j] != cm2[j]:
				diff = True
				if cm1[j] not in aux:
					aux.append(cm1[j])
					graph.append([])
				if cm2[j] not in aux:
					aux.append(cm2[j])
					graph.append([])
				pos = aux.index(cm1[j])
				graph[pos].append(cm2[j])
			j +=1
	hakaiSort(graph,aux)
	return

def main():
	s = stdin.readline().strip("\n")
	diccionario=[]
	while len(s)>0:
		if(s[0]=='#'):
			if len(diccionario)==1:
				print(diccionario[0])
				diccionario=[]
			else:
				solve(diccionario)
				diccionario=[]
		else:
			diccionario.append(s)
		s = stdin.readline().strip("\n")
main()
