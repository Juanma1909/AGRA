from collections import deque
import sys
sys.setrecursionlimit(10000)

c = 0
count = 0
def sumar(dq):
	global c,count		
	if dq[0] == 'p':
		c+=1
		dq.popleft()
		i = 0
		while i < 4:
			if dq[0] == 'p':				
				sumar(dq) 
			elif dq[0] == 'f':
				count += 1024/(4**c)
				dq.popleft()
			else:
				dq.popleft()
			i+=1
		c-=1		
	elif dq[0] == 'f':
		count += 1024/(4**c)
		dq.popleft()
	else:
		dq.popleft()
	return

def tree1n(dq):	
	i = 0
	while i < 4:
		if dq[0] == 'p':
			dq.popleft()				
			tree1n(dq)			
		else:
			dq.popleft()
		i+=1
	return 

def tree1(dq):
	global nt
	i = 0
	while i < 4:
		if dq[0] == 'p':
			dq.popleft()
			nt.append('p')				
			tree1(dq)			
		else:
			nt.append(dq.popleft())
		i+=1
	return

def tree2(dq,qd):
	global nt
	i = 0
	while i < 4:		
		if dq[0] == 'p' and qd[0] == 'p':
			dq.popleft()
			qd.popleft()
			nt.append('p')
			tree2(dq,qd)
		elif dq[0] == 'p' and qd[0] == 'e':
			qd.popleft()
			dq.popleft()
			nt.append('p')
			tree1(dq)
		elif dq[0] == 'e' and qd[0] == 'p':
			dq.popleft()
			qd.popleft()
			nt.append('p')
			tree1(qd)
		elif dq[0]=='f' and qd[0] == 'p':
			nt.append('f')
			dq.popleft()
			qd.popleft()
			tree1n(qd)
		elif dq[0] == 'p' and qd[0] == 'f':
			nt.append('f')
			qd.popleft()
			dq.popleft()
			tree1n(dq)
		elif dq[0] == 'e' and qd[0] == 'e':
			#print("im double e")
			nt.append('e')
			dq.popleft()
			qd.popleft()
		else:
			#print("im else")
			nt.append('f')
			dq.popleft()
			qd.popleft()
		i+=1
	return


def solve(dq,qd):
	global nt,count
	nt = []
	if dq[0] == 'f' or qd[0] == 'f':
		print("There are 1024 black pixels.")
	elif dq[0] == 'e' and qd[0] == 'e':
		print("There are 0 black pixels.")
	elif dq[0] == 'e':
		sumar(qd)
		print("There are "+ str(int(count))+" black pixels.")
	elif qd[0] == 'e':
		sumar(dq)
		print("There are "+ str(int(count))+" black pixels.")
	else:
		qd.popleft()
		dq.popleft()
		nt.append('p')
		tree2(dq,qd)
		#print(nt)
		ntd = deque(nt)
		sumar(ntd)
		print("There are "+ str(int(count))+" black pixels.")
	return



def main():
	global count,c
	
	n = int(sys.stdin.readline().strip())
	for i in range(n):
		c,count = 0,0
		s1 = sys.stdin.readline().strip()		
		s2 = sys.stdin.readline().strip()		
		l1 = list(s1)
		l2 = list(s2)		
		dq = deque(l1)
		qd = deque(l2)		
		solve(dq,qd)

main()
