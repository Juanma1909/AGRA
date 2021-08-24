from sys import stdin
from heapq import heappush,heappop

INF = float('inf')
def solve():
	global G,n,banks,stations
	vis = [False for _ in range(n)]
	dist = [INF for _ in range(n)]
	queue = []
	for i in stations:
		dist[i] = 0
		heappush(queue,(0,i))
	while len(queue) != 0:
		d,u = heappop(queue)
		if vis[u] == False:
			for v,w in G[u]:
				tmpd = d+w
				if tmpd < dist[v]:
					dist[v] = tmpd
					heappush(queue,(tmpd,v))
			if u in banks:
				pass
			else:
				vis[u]=True
	#print(dist)
	newDist = []

	for i in banks:
		newDist.append(dist[i])
	mDist = max(newDist)
	nBanks = newDist.count(mDist)
	indices = [str(banks[i]) for i, x in enumerate(newDist) if x == mDist]
	indices = sorted(indices)
	#print(indices)
	if type(mDist) is int:
		print(str(nBanks) + " " + str(mDist))
	else:
		print(str(nBanks) + " *")

	print(" ".join(indices))

	return dist
def main():
	global G,n,banks,stations
	linea = stdin.readline().strip().split()
	while len(linea) > 0:
		n,m,b,p = int(linea[0]),int(linea[1]),int(linea[2]),int(linea[3])
		G = [[] for _ in range(n)]
		for i in range(m):
			linea = stdin.readline().strip().split()
			u,v,t=int(linea[0]),int(linea[1]),int(linea[2])
			G[u].append((v,t))
			G[v].append((u,t))
		linea = stdin.readline().strip().split()
		banks = []
		stations = []
		for i in range(b):
			banks.append(int(linea[i]))
		linea = stdin.readline().strip().split()
		for i in range(p):
			stations.append(int(linea[i]))
		solve()
		linea = stdin.readline().strip().split()
	return
main()

