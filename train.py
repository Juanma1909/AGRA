from sys import stdin
count = 0
def mergeSort(arr):
  global count
  print("inicio:" + str(arr))  
  if len(arr)>1 :
    mid = len(arr)//2
    leftP = arr[:mid]
    rightP = arr[mid:]
    mergeSort(leftP)
    mergeSort(rightP)    
    i = j = k = d = 0
    print("left: " + str(leftP))
    print("right: " + str(rightP))
    while i < len(leftP) and j < len(rightP):
      if leftP[i] < rightP[j]:
        arr[k]= leftP[i]
        i+=1
        count+=d
      else:
        arr[k] = rightP[j]
        j+=1
        d+=1
      k+=1
    while i < len(leftP):
      arr[k]=leftP[i]
      i+=1
      k+=1
      count += d
    while j < len(rightP):
      arr[k]=rightP[j]
      j+=1
      k+=1
  print("fin: " + str(arr))
  return 0
	
def solve(num, lo, hi):  
  mergeSort(num)
  r = count
  return r

def main():
	global count	
	cases = int(stdin.readline())
	for i in range(cases):
		tam = int(stdin.readline())
		train =[int(x) for x in stdin.readline().strip().split()]				
		count = 0		
		print("Optimal train swapping takes " + str(solve(train,0,tam-1)) + " swaps.")
main()
