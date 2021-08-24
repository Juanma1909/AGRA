from sys import stdin
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
				ap[u] = 1
			if parent[u] != -1 and low[v] >= depth[u]:
				ap[u] = 1
		elif depth[v] < depth[u]:
			low[u] = min(low[u],depth[v])
	return

def tarjan():
	global G	
	n = len(G)
	parent = [-1 for _ in range(n)]
	ap=[0 for _ in range(n)]
	depth = [-1 for _ in range(n)]
	low = [-1 for _ in range(n)]
	for u in range(n):
		if depth[u]==-1:
			depth[u]=low[u]=0
			dfs(u,parent,ap,depth,low)
	
	cap = 0
	for i in range(n):
		if ap[i] == 1:
			cap+=1
	print(cap)
			
	return
def main():
	global G
	n = int(stdin.readline())
	while n != 0:
		G = [[] for _ in range(n)]
		line = stdin.readline().strip().split()
		while len(line)>1:			
			index = int(line[0])-1			
			i = 1
			while i < len(line):
				G[index].append(int(line[i])-1)
				G[int(line[i])-1].append(index)				
				i+=1
			line = stdin.readline().strip().split()
		tarjan()
		n = int(stdin.readline())
	return
main()


		
