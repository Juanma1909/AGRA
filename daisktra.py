from sys import stdin
from heapq import heappush,heappop
INF = float('inf')
"""
def push(h,x):
	h.append(x)
	i = len(h)-1
	while i != 1 and  h[i] < h[i//2]:
		swap(h,i,i//2)
		i = i//2
	return

def top(h):
	return h[1]

def pop(h):
	swap(h,0,len(h)-1)
	x = h.pop()
	i = 1
	m = -1 
	while m != i:
		if j < len(h) and h[j] < h[m] : m = j 
		if k < len(h) and h[k] < h[m] : m = k
	if m != i:
		swap(h,i,m)
		i = m
		m = -1
	return x

def swap(h,i,j):
	h[i],h[j] = h[j],h[i]
	return"""
def solve():
	global s,t,n,G
	vis = [False for _ in range(n)]
	#print(vis)
	dist = [INF for _ in range(n)]
	queue = [(0,s)]
	dist[s] = 0
	parent = [None for _ in range(n)]
	while len(queue) and vis[t] == False:
		d,u = heappop(queue)
		if vis[u] == False:
			vis[u] = True
			for v,w in G[u]:
				tmpd = d+w
				if vis[v] == False and tmpd< dist[v]:
					dist[v] = tmpd
					parent[v] = u
					heappush(queue,(tmpd,v))
	return(dist[t])




def main():
	global s,t,n,G
	cases = int(stdin.readline().strip())
	for case in range(cases):
		line = stdin.readline().strip().split()
		n = int(line[0])
		m = int(line[1])
		s = int(line[2])
		t = int(line[3])
		G = [[] for _ in range(n)]		
		for i in range(m):
			linea = stdin.readline().strip().split()
			u,v,w = int(linea[0]),int(linea[1]),int(linea[2])
			G[u].append((v,w))
			G[v].append((u,w))
		#print(G)		
		ans = solve()
		if (ans)==INF:
			print("Case #" + str(case+1) +": unreachable")
		else:
			print("Case #" + str(case+1) +": " + str(ans))

main()
