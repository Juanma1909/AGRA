from sys import stdin

def dfs(u,vis,val):
	global T,maxD
	tmpmax = 0
	for v in T[u]:
		#print("se está en: " + str(v[0]) + " " + str(v[1]))		
		if vis[v[0]] == False:
			vis[v[0]] = True
			#print("dfs con: " + str(v[0]) + " " + str(v[1]))			
			tmp = dfs(v[0],vis,v[1])
			maxD = max(maxD,tmpmax + tmp)
			tmpmax = max(tmpmax,tmp)

	return tmpmax + val


def solve(n):
	global T,maxD
	vis = [False for _ in range(n)]
	maxD = 0
	for u in range(n):
		#print("estoy en: " + str(u))
		if vis[u] == False:
			vis[u] = True
			maxD = 0
			dfs(u,vis,0)
	print(maxD)
	return

def main():
	global T
	line = stdin.readline().strip().split()	
	while len(line)!=0:
		cases = []
		maxT = 0			
		while len(line) != 0:
			if maxT < max(int(line[0]),int(line[1])):
				maxT = max(int(line[0]),int(line[1]))
			cases.append(line)
			line = stdin.readline().strip().split()
			

		T = [[] for _ in range(maxT)]		
		n = len(cases)
		for i in range(n):
			
			T[int(cases[i][0])-1].append((int(cases[i][1])-1,int(cases[i][2])))
			T[int(cases[i][1])-1].append((int(cases[i][0])-1,int(cases[i][2])))		
		solve(maxT)
		line = stdin.readline().strip().split()	
	return
main()

