from sys import stdin
from heapq import heappush,heappop
INF = float('inf')
def daikstra(e,t):
	global G,n
	vis = [False for _ in range(n)]
	dist =[INF for _ in range(n)]
	queue = [(0,e)]
	dist[e] = 0
	while len(queue) !=0 :
		d,u = heappop(queue)
		if vis[u] == False and d < t :			
			for v,w in G[u]:
				tmpd = d+w
				if tmpd < dist[v]:
					dist[v] = tmpd
					heappush(queue,(tmpd,v))
			vis[u]=True	
	return dist

def solve(e,t):	
	dis = daikstra(e,t)
	#print("i ended")
	mice = 0
	for m in dis:
		if m <= t:
			mice +=1
	print(mice)
	return	


def main():
	global G,n
	cases = int(stdin.readline().strip())
	for i in range(cases):		
		line = stdin.readline().strip()
		n = int(stdin.readline().strip())
		e = int(stdin.readline().strip())-1
		t = int(stdin.readline().strip())
		m = int(stdin.readline().strip())		
		G = [[] for _ in range(n)]
		for j in range(m):
			linea = stdin.readline().strip().split()
			u,v,w = int(linea[0])-1,int(linea[1])-1,int(linea[2])
			G[v].append((u,w))		
		solve(e,t)		
		if i + 1 != cases:
			print()
	return
main()
		


