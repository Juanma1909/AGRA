from sys import stdin
count = 0
def mergeSort(arr):
  global count  
  if len(arr)>1 :
    mid = len(arr)//2
    leftP = arr[:mid]
    rightP = arr[mid:]
    mergeSort(leftP)
    mergeSort(rightP)    
    i = j = k = d = 0
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
  return 0   


def solve(num, lo, hi):  
  mergeSort(num)
  r = count
  
  return r

def main():
  global count
  inp = stdin
  s = inp.readline()
  lab = "Minimum exchange operations : {0}"
  while len(s)>0:
    n = int(s)
    num = [int(x) for x in inp.readline().strip().split()]
    newArr = [None for h in range(n)]
    count = 0
    print(lab.format(solve(num, 0, n-1)))
    s = inp.readline().strip()
  return 0

main()
