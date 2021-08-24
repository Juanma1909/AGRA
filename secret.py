from sys import stdin
def reverse(t):
	net = "  "
	i = len(t)-1
	while i >0:
		net+=t[i]
		i-=1
	return net

def computeFailure(p,r):	
	m = len(p)
	j = 0
	fail = [None for _ in range(m)]
	for i in range(1,m):
		fail[i] = j
		while j > 0 and r[i] != p[j]: 
			j = fail[j]
		j+=1
	return fail
def solve(t):
	r = reverse(t)
	fail= computeFailure(t,r)
	fm = fail.index(max(fail[1:]))
	print(fail)
	print(fm)
	ans = fail[2:fm]
	print (reverse(t[:fm-1])[2:])
	
	return

def main():
	cases = int(stdin.readline().strip())
	for i in range(cases):
		t = " "
		a = stdin.readline().strip()
		t+=a
		solve(t)
	return
main()
