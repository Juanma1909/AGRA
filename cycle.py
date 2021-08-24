from sys import stdin
from collections import deque
def find(x):
	global parent
	if parent[x] != x:
		parent[x] = find(parent[x])
	return parent[x]
	"""if x == parent[x]:
		return x
	else:
		return find(parent[x])"""
def sameC(x,y):
	global parent
	same = False
	if find(x) == find(y):
		same = True
	return same

def union(x,y):
	global parent
	rX = find(x)
	rY = find(y)
	parent[rX] = rY
	return

def solve(edges,n):
	global parent,m	
	e = 0
	i = 0
	T = []
	ans = []
	edges = sorted(edges,key = lambda tup:tup[0])	
	parent = []
	for j in range(n):
		parent.append(j)
	while i < m:
		w = edges[i][0]
		u = edges[i][1]
		v = edges[i][2]			
		if not sameC(u,v) and e != n-1:
			e+=1
			T.append((w,u,v))
			union(u,v)
		else:			
			ans.append(str(w))			
		i+=1
	"""while i < len(edges):
		ans.append(str(edges[i][0]))
		i+=1"""
		
	if (len(ans)==0): print("forest")
	else:
		for i in ans:
			print(i, end = " ")
		print() 
	return




def main():
	global m
	line = stdin.readline().strip().split()
	n,m = int(line[0]),int(line[1])
	while n != 0 or m != 0:		
		edges = []
		for i in range(m):
			line = stdin.readline().strip().split()
			u,v,w = int(line[0]),int(line[1]),int(line[2])			
			edges.append((w,u,v))
		solve(edges,n)
		line = stdin.readline().strip().split()
		n,m = int(line[0]),int(line[1])
	return
main()

""" Codigo guía para implementacion de kruscal: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
	Guia para implementacion de conjuntos disyuntos: https://jariasf.wordpress.com/2012/04/02/disjoint-set-union-find/
	Codigo para impresion: Isabella Acevedo"""
