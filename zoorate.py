age =int(input("enter age:"))
cost=0
while age!=0:
	if age<=2:
		cost=cost+0
	elif age>=2 and age<=12:
			cost=cost+14
	elif age>=65:
				cost=cost+18
	else:
					cost=cost+23
	age=int(input("enter next person age"))				
	print(cost)