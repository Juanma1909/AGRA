from sys import stdin
def solve(dfs,aux):
	pila = []
	graph = [[] for c in range (len(aux))]
	pila.append(dfs[0])

	for x in range (1,len(dfs)-1):		
		if(dfs[x]!= pila[-1]):
			pos = aux.index(pila[-1])
			graph[pos].append(dfs[x])
			pila.append(dfs[x])
		else:
			pila.pop(-1)

	for g in range(len(aux)):
		if(aux[g]==dfs[0]):
			print(aux[g] + " = " + str(len(graph[g])))
		else:	
			print(aux[g] + " = "+ str(1+len(graph[g])))
def main():
	cases = int(stdin.readline())
	i = 0
	while i < cases:
		s = stdin.readline().strip("\n")
		aux = s
		aux = set(aux)
		aux = list(aux)
		aux= sorted(aux)
		print("Case "+ str(i+1))
		solve(s,aux)
		i += 1
	return
main()