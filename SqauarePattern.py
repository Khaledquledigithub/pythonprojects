#Printing square pattern
x =int(input("enter ="))
for i in range(x):
	for j in range(x):
		if( i==0 or i==x-1  or j==0 or j==x-1):
			print("*",end="  ")
		else:
			print("  ",end=" " )
	print()