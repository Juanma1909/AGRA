from sys import stdin
from collections import deque
def solve(l):
	global T
	isit = True
	topo =[]
	n = len(l)
	q = deque()
	indeg={}	
	for j in range(n):
		if l[j] not in indeg:
			indeg[l[j]] = 0
		for h in T[l[j]]:
			if h not in indeg:
				indeg[h] = 0
				indeg[h]+=1
			else:
				indeg[h]+=1
	#print(indeg)
	l2 = list(indeg)

	for j in l2:
		if indeg[j] == 0:
			q.append(j)
			topo.append(j)
		elif indeg[j]!= 1:
			#print("something is not 1")
			isit = False

	if len(q) != 1:
		#print("theres more than one root")
		isit = False
	else:
		while len(q) and isit:
			u = q.pop()
			if u in T:
				for v in T[u]:
					if indeg[v] == 0:
						q.append(v)
						topo.append(v)
					else:
						indeg[v]-=1
						if indeg[v] == 0:
							q.append(v)
							topo.append(v)					
				indeg[u] -=1
	if len(topo) != len(indeg):
		isit = False
	return isit


def next_in():
    global i, s
    while not s[i].isdigit() and s[i] != '-':
        i += 1
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    ans = int(s[i:j])
    i = j
    return ans

i = 0
def main():
	global s,i,T
	s = stdin.read()
	#print(s)	
	cases = 1
	a,b = next_in(),next_in()
	
	while a >= 0 or b >= 0:
		T= {}		
		while a != 0 and b != 0:
			if a not in T:
				T[a] = []
				T[a].append(b)
			else:
				T[a].append(b)
			a,b = next_in(),next_in()
		l = list(T)
		#print(l)
		if len(T) ==0:
			#print("vacio")
			print("Case " + str(cases) + " is a tree.")			
		elif solve(l):
			print("Case " + str(cases) + " is a tree.")
		else:
			print("Case " + str(cases) + " is not a tree.")

		cases +=1
		a,b = next_in(),next_in()			
	return
main()

