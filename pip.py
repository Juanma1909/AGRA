from sys import stdin
def solve(lo,hi,preo,ino):
	global indx,ans
	if lo > hi :
		return
	elif indx < len(preo):
		#print("indx: " +str(indx))
		ind = ino.index(preo[indx])
		#print("lo: " + str(lo) + " hi: "+ str(hi))
		#print(ind)
		if ind>=lo and ind <=hi:
			indx+=1
			#print("indx2: " +str(indx))
			if indx < len(preo):
				solve(lo,ind-1,preo,ino)
				solve(ind,hi,preo,ino)
			ans.append(ino[ind])
def main():
	global indx,ans
	cases = int(stdin.readline())
	for i in range(cases):
		indx = 0
		ans =[]
		prob = stdin.readline().strip().split()
		pre = list(prob[1])
		ins = list(prob[2])
		n = int(prob[0])
		solve(0,n-1,pre,ins)
		print("".join(ans))
	return
main()
