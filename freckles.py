from sys import stdin
from math import sqrt
def find(x):
	global parent
	if x == parent[x]:
		return x
	else:
		return find(parent[x])

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
	global parent
	c = 0
	e = 0
	i = 0
	T = []
	parent = []
	edges = sorted(edges,key = lambda tup:tup[0])
	for j in range(n):
		parent.append(j)
	while e < (n-1):
		w = edges[i][0]
		u = edges[i][1]
		v = edges[i][2]
		if not sameC(u,v):
			e+=1
			c+=w
			T.append((w,u,v))
			union(u,v)
		i+=1
	print("{:.2f}".format(c))
	return


def main():
	cases = int(stdin.readline().strip())
	for i in range(cases):
		line = stdin.readline().strip()
		nF = int(stdin.readline().strip())
		F=[]
		edges = []
		G={}
		for f in range(nF):
			line = stdin.readline().strip().split()
			x = float(line[0])
			y = float(line[1])
			F.append((x,y))
		for f in range(nF-1):
			for g in range(f+1,nF):
				u = f
				v = g
				w = sqrt(((F[u][0]-F[v][0])**2)+((F[u][1]-F[v][1])**2))
				edges.append((w,u,v))
		solve(edges,nF)
		if i + 1 != cases:
			print()
	return
main()




		