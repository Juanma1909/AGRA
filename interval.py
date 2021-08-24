from sys import stdin
class segmentTree:
	def __init__(self, A):
		hojas = 1
		while hojas < len(A):
			hojas*=2
		self.tree = [0 for _ in range(2*hojas)]
		self.tree[0] = 'BASURA'
		for i in range(len(A)):
			self.tree[i+hojas] = A[i]
		for i in reversed(range(1,hojas)):
			self.tree[i] = self.tree[2*i] * self.tree[2*i+1]
		self.hojas = hojas
		return
	def suma(self,lo,hi, i = 1):
		if lo==hi:
			ans = 0
		else:
			ans = self._suma(lo,hi,i=1,L=0 ,R = self.hojas)
		return ans
	def _suma(self, lo,  hi, i, L, R):
		M = (L+R)//2
		if(L == lo and R == hi):
			ans = self.tree[i]
		elif(hi<= M):
			ans = self._suma(lo,hi,2*i,L,M)
		elif(lo >= M):
			ans = self._suma(lo,hi,2*i+1,M,R)
		else:
			ans = self._suma(lo,M,2*i,L,M)
			ans *= self._suma(M,hi,2*i+1,M,R)
		return ans
	def set(self, i, val):
		i = i+self.hojas
		self.tree[i] = val
		while i!=1:
			pa = i//2
			self.tree[pa] = self.tree[2*pa] * self.tree[2*pa+1]
			i = pa
		return

def solve(n,k,array):
	S =  segmentTree(array)
	#print(array)
	#print(S.tree)
	ans = ""
	for i in range(k):
		line = stdin.readline().strip().split()
		if line[0] == 'C':
			S.set(int(line[1])-1,int(line[2]))
		else:
			acum = S.suma(int(line[1])-1,int(line[2]))
			if acum >0:
				ans+="+"
			elif acum == 0:
				ans+="0"
			else:
				ans+="-"
	print(ans)
	return

def main():
	line = stdin.readline().strip().split()	
	while len(line) > 0:
		n,k = int(line[0]),int(line[1])
		array =[int(x) for x in stdin.readline().strip().split()]
		solve(n,k,array)
		line = stdin.readline().strip().split()
		
	return
main()