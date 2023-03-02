#Factorial program
x=int(input("enter no: "))
factorial=1
for i in range(1,x+1):
	factorial=factorial*i
	if x==i:
		print(f"Factorial of {x} is :", factorial)