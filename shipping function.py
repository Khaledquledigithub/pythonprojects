#rate10.95 first order, 2.95 for each item 
def charge(a):
	ship=10.95+(a-1)*2.95
	print(ship)
x=int(input("enter"))
charge(x)