from collections import deque
import sys
sys.setrecursionlimit(10000)
def sumar(L,o,c):
    global find
    if len(L) !=0:
        if len(L[1]) == 0 and len(L[2]) == 0 and find != True:
            c+= L[0]
            if c == o:
                find = True
        elif find != True:
            if len(L[1]) != 0:
                sumar(L[1],o,c+L[0])
            if len(L[2]) != 0:
                sumar(L[2],o,c+L[0])
    return

def my_pop(dq):
	return dq.popleft()

def next(dq):
	return dq[0]

def next_int(dq):
    num = []
    flagMinus = False
    #while (not next(dq).isdigit()) and next(dq) != '-' and len(dq) > 0:        
        #my_pop(dq)
    if next(dq) == '-':
        flagMinus = True
        my_pop(dq)
    num.append(str(next(dq)))
    my_pop(dq)
    while len(dq) > 0 and next(dq).isdigit():
        num.append(str(my_pop(dq)))
    n = len(num)
    if flagMinus:
        ans = int("".join(num))*-1
    else:
        ans = int("".join(num))

    #print("heres dq " + str(next(dq)))
    #print(str(ans))
    return ans

def parse(dq):
    assert my_pop(dq) == '('
    #print("srtart here: " + str(next(dq)))
    tree = []
    if next(dq) != ')':    
    	num = next_int(dq)
    	#print("this is the num " + str(num))
    	tree.append(num)
    while next(dq) != ')':
        x = parse(dq)
        tree.append(x)        
    my_pop(dq)    
    return tree

def main():
    global find
    #case = 0
    find = False
    s = sys.stdin.read()
    s = s.replace("\n","")
    s = s.replace(" ","")
    #print(s)    
    q = deque(s)
    while len(q):
        #case +=1
        find = False
        o = next_int(q)      
        tree = parse(q)
        #print("case" + str(case) + ": " + str(tree))
        sumar(tree,o,0)
        if find == False:
            print("no")
        else:
            print("yes")
main()
