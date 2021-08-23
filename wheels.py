from sys import stdin
from collections import deque

def sumar(num):
	newnum1 = 0
	newnum2 = 0
	ans=[]
	for i in range(4):
		tmp1 = num//10**i
		tmp2 = num//10**i
		if (tmp1%10) + 1 > 9:
			newnum1 = num - (tmp1%10)*(10**i)
		else:
			newnum1 = num + 1*(10**i)

		if (tmp2%10) - 1 < 0:
			newnum2 = num + 9*(10**i)
		else:
			newnum2 = num - 1*(10**i)
		ans.append(newnum1)
		ans.append(newnum2)
	return ans


def to_num(arr):
	num = 0
	num+= int(arr[0])*1000
	num+= int(arr[1])*100
	num+= int(arr[2])*10
	num+= int(arr[3])
	return num
	
grafo=[sumar(x) for x in range(10000)]

def solve(ini,fin):
	global vis,count
	if(vis[fin] == True):
		print(-1)
		return 0
	queue = deque()
	queue.append(ini)		
	found = False
	while len(queue) != 0 and found == False:
		u = queue.popleft()
		#print("u: " + str(u))
		if u == fin:
			found = True
			print(str(count[fin]))
			return 0
		else:
			for tmp in grafo[u]:
				if vis[tmp] == False:
					vis[tmp] = True
					count[tmp] = count[u] + 1
					queue.append(tmp)
	if found == False:
		print(-1)	
	return 0


def main():
	global vis,count 	
	cases = int(stdin.readline())
	Cvis = [False for _ in range(10000)]
	Ccount = [0 for _ in range(10000)]
	for i in range(cases):		
		linea = stdin.readline()		
		vis = Cvis.copy()
		count = Ccount.copy()
		s = stdin.readline().strip().split()
		ini =  to_num(s) #[int(x) for x in s]			
		count[ini] = 0		
		s = stdin.readline().strip().split()
		fin	= to_num(s) #[int(x) for x in s]				
		numF = int(stdin.readline())		
		for j in range(numF):
			f = stdin.readline().strip().split()			
			vis[to_num(f)]=True
		solve(ini,fin)		
	return 0		
		
main()


