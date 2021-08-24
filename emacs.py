from sys import stdin
def calculatepi(p):
	#print("calculating prefixs")
	#print(p)
	l = len(p)
	pi = [0]
	k = 0
	for i in range(1,l):
		while(k > 0 and p[k] != p[i]):
			k = pi[k-1]
		if(p[k]==p[i]):
			k = k+1
		pi.append(k)
	return pi
def KMP(p,t):
	global index
	m = len(p)
	n = len(t)
	j = 0
	lps = calculatepi(p)
	while index < n:
		if p[j] ==t[index]:
			index+=1
			j+=1
		if j == m:
			return True
			j = lps[j-1]
		elif index < n and p[j] != t[index]:
			if j != 0:
				j = lps[j-1]
			else:
				index+=1
	return False
def solve(t,p):
	#print(p)
	#print(t)
	global index
	finds = []
	index = 0
	for j in p:
		s = KMP(j,t)
		finds.append(s)
	if False in finds:
		print("no")
	else:
		print("yes")
	return
def split(s):
	news = []
	n = len(s)
	mini =""
	for i in range(n):
		if s[i] != '*':
			mini+=s[i]
		elif mini != "":
			news.append(mini)
			mini = ""
	if mini != "":
		news.append(mini)
	return news

def main():
	cases = stdin.readline().strip()
	while len(cases)>0:
		t = stdin.readline().strip()
		cases = int(cases)
		for i in range(cases):
			p = stdin.readline().strip()
			p = split(p)
			#print(p)
			solve(t,p)
		cases = stdin.readline().strip()		
	return
main()

