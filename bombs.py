import sys
sys.setrecursionlimit(10000)
def imp(pv):
	global m	
	l = list(pv)
	l = sorted(l,reverse = True)
	#print(l)
	for h in l:
		pv[h] = sorted(pv[h])

	i=p=0
	while p < m:
		j = 0
		while p < m and j < len (pv[l[i]]):
			print(str(pv[l[i]][j]) + " " + str(l[i]))
			p+=1
			j +=1
		i+=1
	return

def dfs(u,parent,ap,depth,low):
	global G
	children = 0

	for v in G[u]:
		if depth[v] ==-1:
			depth[v] = low[v] = depth[u]+1
			parent[v] = u
			children+=1
			dfs(v,parent,ap,depth,low)
			low[u] = min(low[u],low[v])
			if parent[u] == -1 and children > 1:
				ap[u] +=1
			if parent[u] != -1 and low[v] >= depth[u]:
				ap[u] +=1
		elif depth[v] < depth[u]:
			low[u] = min(low[u],depth[v])
	return

def tarjan(l,n):
	global G
	parent = [-1 for _ in range(n)]
	ap = [0 for _ in range(n)]
	depth = [-1 for _ in range(n)]
	low = [-1 for _ in range(n)]
	for u in range(n):
		#i = l[u]
		if depth[u] == -1:
			depth[u] = low[u]=0
			dfs(u,parent,ap,depth,low)

	for i in range(n):
		ap[i]+=1
	pv= {}
	for i in range(n):
		if ap[i] not in pv:
			pv[ap[i]]=[]
			pv[ap[i]].append(i)
		else:
			pv[ap[i]].append(i)	
	imp(pv)
	print()


def main():
	global G,m	
	line = sys.stdin.readline().strip().split()
	a,b = int(line[0]),int(line[1])
	n = a
	m = b
	while a!=0 and b!=0:
		linea = sys.stdin.readline().strip().split()
		G = {}
		for i in range(n):
			G[i] = []
		a,b = int(linea[0]),int(linea[1])
		while a >= 0 and b >=0:			
			G[a].append(b)			
			G[b].append(a)
			linea = sys.stdin.readline().strip().split()
			a,b = int(linea[0]),int(linea[1])

		
		l = list(G)		
		tarjan(l,n)
		line = sys.stdin.readline().strip().split()
		a,b = int(line[0]),int(line[1])
		n = a
		m = b
	return
main()



		
