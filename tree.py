G=[]
def dfs(u,o,cont):
	global G
	cont+=u
	if cont == o:
		print("yes")
		found = True
	if found != True:
		for v in G[u]:
			if vis[v] == False:
				vis[v] = True
				cont += dfs(u,o,cont)
	return

def main():
	global G
	found = False
	n = len(G)
	vis =[False for _ in range(n)]
	for u in range(n):
		if vis[u] == False:
			vis[u] = True
			dfs(u,o,0)
			if found == False:
				print("no")