from sys import stdin
from collections import deque
def dfs(u,num):
	global vis, scc,G
	vis[u] = 1
	scc[u] = num
	for v in G[u]:
		if(vis[v] == 0):
			dfs(v,num)
	return

def dfs_list(u):
	global L, vis, I,G
	vis[u] = 1
	for v in I[u]:
		if(vis[v] == 0):
			dfs_list(v)
	L.append(u)
	return


def compute():
	global L,I, scc, vis,G
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
			dfs_list(i)
	vis = [0 for i in range(n)]
	cont = 0
	while(len(L)):
		i = L.pop()
		if(vis[i] == 0):
			dfs(i,cont)
			cont +=	1
	print(cont)
	return 


def main():
	global G	
	line = stdin.readline().strip().split()
	while int(line[0])!=0 or int(line[1])!= 0:			
		p = int(line[0])
		t = int(line[1])
		G = [[] for _ in range(p)]		
		aux={}
		for i in range(p):
			person = stdin.readline().strip("\n")
			aux[person] = i			
		for i in range(t):			
			q = stdin.readline().strip("\n")			
			G[aux[q]].append(aux[stdin.readline().strip("\n")])						
		compute()
		line = stdin.readline().strip().split()
	return
main()

