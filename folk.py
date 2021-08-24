def folk(arr,s,i,c):
	f = ""		
	if(i==len(arr)):
		print(c)
		return c
	else:
		s+=arr[i]
		c+=s
		folk(arr,s,i+1,c)

r = ["pio","moo","miau","guau"]
folk(r,"",0,"")

