age=int(input("Enter age: "))
cost1=0
while age!=0:
	if age<=2:
		cost1=cost1+0
	elif age>=3 and age<=12:
		cost1=cost1+14
	elif age<=65 and age>=15:
		cost1=cost1+18
	else:
		cost1=cost1+23
	print("Total cost: ",cost1)
	age=int(input("Enter another age: "))
