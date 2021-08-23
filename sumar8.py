def to_num(arr):	
	num = 0
	num+= arr[0]*1000
	num+= arr[1]*100
	num+= arr[2]*10
	num+= arr[3]
	"""for x in arr:
		num += int(x)*(10**(3-i))
		i += 1"""
	return num
	
def sumar(num):
	newnum1 = 0
	newnum2 = 0
	for i in range(4):
		tmp1 = num//10**i
		tmp2 = num//10**i
		if (tmp1%10) + 1 > 9:
			newnum1 = num - (tmp1%10)*(10**i)
		else:
			newnum1 = num + 1*(10**i)

		if (tmp2%10) - 1 < 0:
			newnum2 = num + 9*(10**i)
		else:
			newnum2 = num - 1*(10**i)

		print(newnum1)
		print(newnum2)

