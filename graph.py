T = [[1],[0],[3],[2,4],[3]]

def list_to_mat(G):
	tam = len(G)
	M = [[0 for j in range(tam)] for k in range (tam)]
	for i in range(tam):
		for j in G[i]:
			M[i][j] = 1
	return M

for l in list_to_mat(T):
	print(l)

def mat_to_list(M):
	tam = len(M)
	l = [ [] for i in range(tam)]
	for i in range(tam):
		for j in range(tam):
			if M[i][j]==1:
				l[i].append(j)
	return l
for li in mat_to_list(list_to_mat(T)):
	print(li)
def list_to_arc(L):
	tam = len(L)
	E=[]
	for i in range(L):
		for j in range(L):
			E.append((i,j))
	return E,tam
def arc_to_list(A,tam):
	li = [[] for i in range(tam)]
	for i,j in A:
		li.append(j) 
	return li
for j in arc_to_list(list_to_arc(T)):
	print(j)
def bsf(src,G,vis):
	q = deque()
	q.append(src)
	vis[src] = 1
	while len(q):
		u = q.pop() """pop es para dfs(profundidad) y popleft para bfs"""
		for v in G[u]:
			if vis[v]==0:
				vis[v]=1
				q.append(v)
	return
def dfs(u,G,vis):
	vis[u]=1
	for v in G[u]:
		if vis[v] ==0:
			dfs(v,G,vis)
	return
G = 
def count_CCs(G):
	tam = len(G)
	count = 0
	vis = [0 for i in range(tam)]
	for u in range(tam):
		if vis[u] == 0:
			dfs(u,G,vis)
			count +=1
	return count
def hakaisort(G):
	n = len(G)
	indeg=[0 for i in range(n)]
	for u in range(n):
		for v in G[u]:
			#hay un arco u-->v
			indeg[v]+=1
	topo=[]
	while len(topo)<n:
		for i in range(n):
			if indeg[i]==0:
				topo.append(i)
				for j in G[i]:
					indeg[j]-=1
				indeg[i]=-1
	return topo



