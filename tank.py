from sys import stdin
def main():
	line = stdin.readline().strip().split()
	while len(line) > 0:
		n,m = int(line[0]),int(line[1])
		citiesP = stdin.readline().strip().split()
		G = [[] for _ in range(n)]
		for i in range(m):
			line = stdin.readline().strip().split()
			G[line[0]].append((line[1],line[2]))
			G[line[1]].append((line[0],line[2]))
		q = int(stdin.readline().strip())
		for j in range(q):
			line = stdin.readline().strip().split()
			c,s,e = int(line[0]),int(line[1]),int(line[2])
			

