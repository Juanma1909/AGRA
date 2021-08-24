from sys import stdin
def sRight(ladies,x,lo,hi):
        while lo < hi:
                mid = (lo + hi)//2
                if x < ladies[mid]:
                        hi = mid
                else:
                        lo = mid + 1
        return lo
        
def sLeft(ladies,x,lo,hi):
        while lo < hi:
                mid = (lo + hi)//2
                if x > ladies[mid]:
                        lo = mid + 1
                else:
                        hi = mid
        return lo
def solve(ladies, x):
        hi = len(ladies)
        lo = 0
        ansR,ansL = None,None
        minR,maxL=0,0
        maxL = sLeft(ladies,x,lo,hi)
        minR = sRight(ladies,x,lo,hi)        
        if minR > len(ladies)-1:
                print(str(ladies[maxL-1])+" "+"x")
        else:
                print(str(ladies[maxL-1])+" "+str(ladies[minR]))
	
	
                
def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    solve(ladies, x)
    
main()

