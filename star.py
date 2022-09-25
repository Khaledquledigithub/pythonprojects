n=int(input("enter="))
for i in range(n):
	for j in range(n):
		if i>=j:
			print("*",end=" ")
	print(" ")