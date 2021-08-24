from sys import stdin
def dfs(i,j,especie,arbol,n,m):
	global monos,matriz
	q = []
	t = (i,j)
	q.append(t)
	monos[i][j] = especie
	while len(q)>0:		
		u = q.pop() 
		i = u[0]
		j = u[1]		
		if(i-1 < 0 or j-1 < 0 ):
			pass
		else:
			if(matriz[i-1][j-1] == arbol):
				if(monos[i-1][j-1]==0):
					monos[i-1][j-1]=especie
					t = (i-1,j-1)
					q.append(t)
		if(i < 0 or j-1 < 0 ):
			pass
		else:
			if(matriz[i][j-1] == arbol):
				if(monos[i][j-1]==0):
					monos[i][j-1]=especie
					t = (i,j-1)
					q.append(t)
		if(i+1 >= n or j-1 < 0 ):
			pass
		else:
			if(matriz[i+1][j-1] == arbol):
				if(monos[i+1][j-1]==0):
					monos[i+1][j-1]=especie
					t = (i+1,j-1)
					q.append(t)
		if(i+1 >= n or j < 0):
			pass
		else:
			if(matriz[i+1][j] == arbol):
				if(monos[i+1][j]==0):
					monos[i+1][j]=especie
					t = (i+1,j)
					q.append(t)
		if(i+1 >= n or j+1 >= m):
			pass
		else:
			if(matriz[i+1][j+1] == arbol):
				if(monos[i+1][j+1]==0):
					monos[i+1][j+1]=especie
					t = (i+1,j+1)
					q.append(t)
		if(i < 0 or j+1 >= m):
			pass
		else:
			if(matriz[i][j+1] == arbol):
				if(monos[i][j+1]==0):
					monos[i][j+1]=especie
					t = (i,j+1)
					q.append(t)
		if(i-1 < 0 or j+1 >= m):
			pass
		else:
			if(matriz[i-1][j+1] == arbol):
				if(monos[i-1][j+1]==0):
					monos[i-1][j+1]=especie
					t = (i-1,j+1)
					q.append(t)
		if(i-1 < 0 or j < 0 ):
			pass
		else:
			if(matriz[i-1][j] == arbol):
				if(monos[i-1][j]==0):
					monos[i-1][j]=especie
					t = (i-1,j)
					q.append(t)			
	return

def solve():
	global monos,matriz	
	especie = 0
	n = len(matriz)
	m = len(matriz[0])	
	monos = [[] for i in range(n)]
	for x in range(n):
		for z in range(m):
			monos[x].append(0)		
	for i in range(n):
		for j in range(m):
			if monos[i][j] == 0:
				especie+=1
				dfs(i,j,especie,matriz[i][j],n,m)


	for i in range(len(monos)):
		monos[i] = list(map(str,monos[i]))
	tama =[]
	for j in range(len(monos[0])):
		maximp = 0
		for i in range(len(monos)):
			if len(monos[i][j]) > maximp:
				maximp = len(monos[i][j])
		tama.append(maximp)
	for i in range(len(monos)):
		for j in range(len(monos[i])):
			if(j != 0):
				print(''.join(monos[i][j].rjust(tama[j]+1)), end = "")
			else:
				print(''.join(monos[i][j].rjust(tama[j])), end = "")
		print()
	print("%")





	
def main():
	global matriz
	matriz = []
	m = stdin.readline().split()
	while len(m)>0:				
		if m[0] != '%':
			matriz.append(m)
		else:
			solve()			
			matriz = []
		m = stdin.readline().split()
	solve()
main()
"""colaboradores: Nicolas Ibagón"""