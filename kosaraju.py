def dfs(u,num):
	global vis, scc, G
	vis[u] = 1
	scc[u] = num
	for v in G[u]:
		if(vis[v] == 0):
			dfs(v,num)
	return

def dfs_list(u):
	global L, vis, I
	vis[u] = 1
	for v in I[u]:
		if(vis[v] == 0):
			dfs_list(v)
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
			dfs_list(i)
	vis = [0 for i in range(n)]
	cont = 0
	while(len(L)):
		i = L.pop()
		if(vis[i] == 0):
			dfs(i,cont)
			cont +=	1
	return scc

G = [
	[3,7],
	[0],
	[1],
	[3],
	[],
	[4,6],
	[5],
	[1,5,8],
	[0,6],
	[1]
]

scc = compute(G)
for i,x in enumerate(scc):
	print(i,x)

